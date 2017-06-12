#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json


with open('dataset.json') as data_file:    
    data = json.load(data_file)



f = open('dataset.txt', 'w')
for i in range(len(data)):
    n = len(data[i]["sentences"])
    for j in range(len(data[i]["sentences"])):
        f.write(data[i]["sentences"][j]["sentenceSpeaker"])
        f.write(";")
        f.write(data[i]["sentences"][j]["sentenceTime"])
        f.write(";")
        f.write(data[i]["sentences"][j]["sentenceContent"].encode('utf-8'))
        f.write("\n")
f.close()