#!/usr/bin/python3
# -*- coding: utf-8 -*

import csv
import pathlib as pl

pass_data="./data_calib"
pass_out="./001.dat"

def gen_lact(pass_datatmp,pass_outtmp):
    xmax = -100
    xmin = 100
    ymax = -100
    ymin = 100
    p_temp = pl.Path(pass_datatmp).glob("*pca.csv")
    for p in p_temp:

        with p.open() as f:
            reader=csv.reader(f)

            fout = open(pass_outtmp, 'w')

            fcon=0

            for row in reader:
                if fcon == 0:
                    if float(row[0]) >= xmax:
                        xmax = float(row[0])
                    if float(row[0]) <= xmin:
                        xmin = float(row[0])

                elif fcon == 1:
                    if float(row[0]) >= ymax:
                        ymax = float(row[0])
                    if float(row[0]) <= ymin:
                        ymin = float(row[0])

                fcon = fcon + 1

            fout.write(str(xmax) + ',' + str(ymax)+ ',' + str(xmin)+ ',' + str(ymin))

            fout.close()
        f.close()
        
if __name__ == "__main__":
    gen_lact(pass_data,pass_out)

