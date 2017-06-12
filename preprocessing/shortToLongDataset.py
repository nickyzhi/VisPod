#! /usr/bin/env python
# -*- coding: utf-8 -*-

with open("shortSenDataset.txt") as f:
    content = f.readlines()
f.close()
dataset = []
for i in range(len(content)):
    lineArray = content[i].split(";")
    lineArray[-1] = lineArray[-1].strip('\n')
    dataset.append([])
    dataset[i].append(lineArray[0])
    dataset[i].append(lineArray[1])
    dataset[i].append(' '.join(lineArray[2:]))

f = open('dataset.txt', 'w')

for i in range(len(dataset)):
    if i == 0:
        f.write(dataset[i][0])
        f.write(";")
        f.write(dataset[i][1])
        f.write(";")
        f.write(dataset[i][2])
    else:
        if dataset[i][0] == dataset[i-1][0]:
            f.write(" "+ dataset[i][2])
        else:
            f.write("\n")
            f.write(dataset[i][0])
            f.write(";")
            f.write(dataset[i][1])
            f.write(";")
            f.write(dataset[i][2])

f.close()

