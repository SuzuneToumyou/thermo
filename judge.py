#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import pathlib as pl

pass_lact="./001.dat"
pass_data="./data_e"

#import pathlib as pl

#def



if __name__ == '__main__':
    f = open(pass_lact, 'r')


    data = f.readline()
    data = data.replace("\n", "")
    l = data.split(",")

    max_x=l[0]
    max_y=l[1]
    min_x=l[2]
    min_y=l[3]

    dummy_x=0
    dummy_y=0

    p_temp = pl.Path(pass_data).glob("*pca.csv")
    for p in p_temp:
        with p.open() as f_2:

            #f_2 = open('data_e/pospca.csv', 'r')

            fcon = 0
            reader=csv.reader(f_2)
            for row in reader:
                if fcon == 0:
                    dummy_x = float(row[0])
                if fcon == 1:
                    dummy_y = float(row[0])
                fcon = fcon + 1

            if dummy_x <= float(max_x) and dummy_x >= float(min_x) and dummy_y <= float(max_y) and dummy_y >= float(min_y):
                print ("nomal")
            else :
                print ("abnomal")

            f_2.close()

    f.close()

