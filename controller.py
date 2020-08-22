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
SCALE=int(SCALE)
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

elif(len(argv)>1 and (argv[1]=='--query' or argv[1]=='-q')):
    query(value,MINVALUE,MAXVALUE)

else:
    print('No option selected.\
        \nPossible options are:\
            \n\n--increase (-i):\tTo increase the brightness by scale\
            \n--decrease (-d):\tTo decrease the brightness by scale\
            \n--query (-q):\t\tTo run a query for present status')