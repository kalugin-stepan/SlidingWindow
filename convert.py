import numpy as np
import argparse
import os
import os.path as path

parser = argparse.ArgumentParser()

parser.add_argument('-i', required=True)
parser.add_argument('-o', required=True)

args = parser.parse_args()

def convert_file(fin_path: str, fout_path: str):
    fin = open(fin_path, 'rb')
    fout = open(fout_path, 'w')
    while True:
        data = fin.read(2 * 8)
        if len(data) != 2 * 8: break
        data = np.frombuffer(data, dtype=np.int16)
        fout.write('"')
        for i in range(len(data)):
            fout.write(str(data[i]))
            if i != len(data) - 1: fout.write('","')
        fout.write('"\n')

    fin.close()
    fout.close()

if path.isfile(args.i) and path.isfile(args.o):
    convert_file(args.i, args.o)
elif path.isdir(args.i) and path.isdir(args.o):
    for i in os.listdir(args.i):
        convert_file(path.join(args.i, i), path.join(args.o, i.split('.')[0] + '.csv'))
else:
    print('???')