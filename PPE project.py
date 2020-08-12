#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:10:30 2020

@author: Shragvi
"""

import pandas as pd
import numpy as np

datatot = pd.read_csv("/Users/Shragvi/downloads/daily.csv")
print(datatot)
dates= ['20200122','20200222','20200322','20200322','20200422','20200522','20200622']
print(dates)

print(datatot)
states= list()
for k in range(len(datatot)):
    statestr= str(datatot.loc[k,'state'])
    if (statestr in states):
        continue
    else:
        states.append(statestr)
print(states)  
dct = {}
for k in states:
     dct['%s' % k]=[k]
print (dct)

for k in range(len(datatot)):
    datestr= str(datatot.loc[k,'date'])
    if datestr in dates:
        statestr= str(datatot.loc[k, 'state'])
        for j in dct:
            if statestr in j:
                posstr= str(datatot.loc[k,'positive'])
                if posstr== 'nan':
                    dct[j].append('0.0')
                else:
                    dct[j].append(posstr)
 
print(dct)  
totavg= 0
avg = {}
sum1= 0
for i in states:
    avg['%s' % i] = []   
    
for i in dct:
    sum1=0
    for j in range(len(dct[i])):
        if j==0 :
            continue
        else:
            val= dct[i][j]
            valint= float(val)
            sum1= sum1+valint   
    tempavg= sum1/6
    totavg=totavg+tempavg
    avg[i].append(tempavg)
    
              
tempavg=0
sum1=0
perc=0           
percent= {} 
for i in states:
    percent['%s' % i] = []   
    
for i in avg:
    sum1=0
    for j in range(len(dct[i])):
        if j==0 :
            continue
        else:
            val= dct[i][j]
            valint= float(val)
            sum1= sum1+valint
    tempavg= sum1/6
    xpercent= (tempavg/totavg)*100
    percent[i].append(xpercent)
    perc = perc+ xpercent
print(percent)
print(perc)


                
 