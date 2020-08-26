#!/bin/env python3
import sys
import os
from sys import argv
path="/sys/class/backlight/intel_backlight"
filename="brightness"

def increase(value, MAXVALUE, scale):
    file=open(path+'/'+filename,'w')
    file.write(str(min(value+scale,MAXVALUE)))
    file.close

def decrease(value, MINVALUE, scale):
    file=open(path+'/'+filename,'w')
    file.write(str(max(value-scale,MINVALUE)))
    file.close

def query(value,MINVALUE,MAXVALUE):
    print("Current Brightness level:",100-int((MAXVALUE-value)*100/(MAXVALUE-MINVALUE)),"%")
    print("Current Brightness sensitivity:",SCALE*100//(MAXVALUE-MINVALUE),"%")

file=open(path+'/'+filename,'r')
value=file.read().split('\n')[0]
value=int(value)
file.close()

file=open('maxvalue','r')
MAXVALUE=file.read().split('\n')[0]
MAXVALUE=int(MAXVALUE)
file.close()

file=open('minvalue','r')
MINVALUE=file.read().split('\n')[0]
MINVALUE=int(MINVALUE)
file.close()

file=open('scale','r')
SCALE=file.read().split('\n')[0]
try:
    SCALE=int(SCALE)
except:
    SCALE=5*(MAXVALUE-MINVALUE)//100
file.close()

if(len(argv)>1 and (argv[1]=='--increase' or argv[1]=='-i')):
    print('Increasing brightness...')
    if(value==MAXVALUE):
        print('Maximum brightness level achieved...')
    increase(value, MAXVALUE,SCALE)

elif(len(argv)>1 and (argv[1]=='--decrease' or argv[1]=='-d')):
    print('decreasing brightness...')
    if(value==MINVALUE):
        print('Minimum brightness level achieved...')
    decrease(value,MINVALUE,SCALE)

elif(len(argv)>1 and (argv[1]=='--sensitivity' or argv[1]=='-s')):
    if len(argv)<=2 or not(1<=int(argv[2])<=99):
        print("Aborting... no/invalid scale value passed...")
        print("Brightness Scale must be between 1 and 99 percent.")
        exit()
    print('Changing brightness change scale to:',argv[2],"%")
    Range=MAXVALUE-MINVALUE
    file=open('scale','w')
    file.write(str(int(argv[2])*Range//100))
    file.close()

elif(len(argv)>1 and (argv[1]=='--query' or argv[1]=='-q')):
    query(value,MINVALUE,MAXVALUE)

elif(len(argv)>1 and (argv[1]=='--default' or argv[1]=='-z')):
    Range=MAXVALUE-MINVALUE
    file=open('scale','w')
    file.write(str(int(5)*Range//100))
    file.close()

else:
    print('No option selected.\
            \nPossible options are:\
            \n\n--increase (-i):\tTo increase the brightness by scale\
            \n--decrease (-d):\tTo decrease the brightness by scale\
            \n--query (-q):\t\tTo run a query for present status\
            \n--sensitivity (-s) [SCALE]:\tTo change the percentage change in brightness for every increase or decrease in brightness.\
            \n--default (-z):\tTo reset settings to original settings.\
        \n')
    exit()
