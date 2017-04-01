import csv
import numpy as np
import json
import jsonpickle


varArray = []
values = []
calls = []


paramArray = []
i = 0

def inArray(array, argument):
    for item in array:
        if (item == argument):
            return true
        else:
            return false

def defineValuePair(key, value):
    valuePairs.append({key: value})

class parameter:
    name = ""
    values = {}

    def increment(self, key):
    
        if key in self.values:
            self.values[key] = self.values[key] + 1
        else:
            self.values[key]=0
            paramArray.append(self)
        

    def __init__(self, paramName):
        self.name = paramName
        self.values = {}
        self.dependants = {}
       
    def __iter__(self):
        return iter(self.values)
    def defineDependencies(self):
        dependants = {}
        for key in self.values:
            valName = key
            freq = self.values[key]
            for i in range(0, len(values)):
                if (varArray[i] == self.name) and (values[i] == valName):
                    index = 0 
                    while(calls[i] == calls[index]): 
                        if not (varArray[index] == self.name):
                            if varArray[index] in dependants:
                                if values[index] in dependants[varArray[index]]:
                                    dependants[varArray[index]][values[index]] = dependants[varArray[index]][values[index]] + 1
                                else:
                                    dependants[varArray[index]][values[index]] = 1
                            else:
                                dependants[varArray[index]] = {}
                                dependants[varArray[index]][values[index]] = 1

                        index = index + 1
                        if (index >= len(calls)):
                            break
    
            self.values[key] = {'dependancies':dependants}
     
        


class functionJSON:
    name = ""
    parameters = {}
    def __init__(self, functName, param):
        self.name = functName
        self.parameters = param

with open('C:/Users/DSmith/Documents/caseForDynamicQuery/test10-ssh_channel_read.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    
    for row in spamreader:
        print(i)
        print("stats")
        i = i + 1
        if (row[0] == "Function"):
            continue
        else:
            functName = row[0]

  
        varArray.append(row[2])
        values.append(row[6])
        calls.append(row[1])

    for name in varArray:
       obj = parameter(name)
       paramArray.append(obj) 

    funct = functionJSON(functName, paramArray)

    for i in range(0, len(values)):
        for item in paramArray:
            
            if (varArray[i] == item.name):
                item.increment(values[i])
                
                print("added item")

    #for obj in paramArray:
       # obj.defineDependencies()

    funct = functionJSON(functName, paramArray)

    print ("{")
    print ('"fname": ', funct.name, ",")
    print ('"vars": [')
    for parameter in paramArray:
        print ("{")
        print ('"vname": ', parameter.name)
        print ('"concordance": [')
        for key in parameter.values:
            print ("{")
            print ('"possibleVal": ', key)
            print ('"frequency":', parameter.values[key])
            print("}")
        print("]")
        print("}")
    print("]")
    print("}")

    for obj in paramArray:
        obj.defineDependencies()

    funct = functionJSON(functName, paramArray)

    print("[")
    print("{")
    for parameter in paramArray:
        for key in parameter:
            print('"vname": ',key)
            print(parameter.values[key])
    print("}")
    print("]")



