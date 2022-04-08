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

from bitarray import bitarray

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
    #count, result = pi.i2c_read_device(h,1024)
    time.sleep(2)

    pi.i2c_close(h)
    #now_date = datetime.datetime.now()
    #now = now_date.strftime("%Y%m%d%H%M")

    tP = []
    if count <= 0: 
        return (0)
    else:
        #file_name= pass_datatmp + str(now) + ".csv"
        file_name="./outputdata.dat"
        fout= open(file_name,"wb")
        #writer = csv.writer(fout)

        #readbuff = bytes(result,'utf-8')
        readbuff = bytes(result)

        fout.write(readbuff)
        #print(readbuff)
        #print(readbuff.hex())

        #bits = bitarray(endian='big')
        #bits.frombytes(readbuff)
        #print(bits.to01())

        #for i in readbuff:
        #       print(readbuff[i])
        #    print((readbuff[i]))
        #fout.close()

        tPTAT = (256*readbuff[1] + readbuff[0])/10

        for i in range(1025):
        #for i in range(00):
            if i != 0:
                tmp = (256*readbuff[i*2+1] + readbuff[i*2])/10
                #tP.append([tmp, (i-1)%32, math.floor((i-1)/32)])

        #tP2=sorted(tP,reverse=True,key=lambda x: x[0])
        #del tP2[250:]
        #writer.writerows(tP2)
        #fout.close()

        #data_T = tP2.T
        #data_T.shape

        #pca = PCA(n_components=1)
        #X2D = pca.fit_transform(tP2)
        #X2D.shape

        #file_name2 = pass_datatmp + str(now) + "pca.csv"
        #fout2=open(file_name2 ,"w")
        #np.savetxt(fout2,X2D,delimiter=",")
        #fout2.close()

        return(1)
    tP.clear()
    pi.i2c_close(h)

if __name__ == "__main__":

    return_data = senser_get(pass_data)
    if return_data != 0:
        return_data = senser_get(pass_data)
    time.sleep(10)
    return_data = senser_get(pass_data)
