#!/usr/bin/python3
# -*- coding: utf-8 -*

import pigpio
import time
import struct

import math
import csv

import numpy as np
from sklearn.decomposition import PCA
import pathlib as pl

import datetime

pass_data = "./data_e/"

def senser_get(pass_datatmp):
    pi = pigpio.pi()
    addr = 0x0a

    h = pi.i2c_open(1,addr) # ハンドル取得

    #try:
    #    pi.i2c_write_quick(h, 0) # AM2322のスリープ解除
    #except:
    #    pass

    pi.i2c_write_device(h, [0x4d])
    time.sleep(2)
    count, result = pi.i2c_read_device(h,2051)
    time.sleep(2)

    now_date = datetime.datetime.now()
    now = now_date.strftime("%Y%m%d%H%M")

    tP = []
    if count > 0:
        file_name= pass_datatmp + str(now) + ".csv"
        fout= open(file_name,"w")
        writer = csv.writer(fout)

        readbuff = bytes(result)

        tPTAT = (256*readbuff[1] + readbuff[0])/10

        for i in range(1025):
            if i != 0:
                tmp = (256*readbuff[i*2+1] + readbuff[i*2])/10
                tP.append([tmp, (i-1)%32, math.floor((i-1)/32)])

        tP2=sorted(tP,reverse=True,key=lambda x: x[0])
        del tP2[250:]
        writer.writerows(tP2)
        fout.close()

        #data_T = tP2.T
        #data_T.shape

        pca = PCA(n_components=1)
        X2D = pca.fit_transform(tP2)
        X2D.shape

        file_name2 = pass_datatmp + str(now) + "pca.csv"
        fout2=open(file_name2 ,"w")
        np.savetxt(fout2,X2D,delimiter=",")
        fout2.close()

        return(1)
    else :
        return(0)

    tP.clear()
    pi.i2c_close(h)

if __name__ == "__main__":

    return_data = senser_get(pass_data)
    if return_data != 0:
        return_data = senser_get(pass_data)
    time.sleep(10)
    return_data = senser_get(pass_data)
