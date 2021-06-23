import csv
import random
import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection, Error
import openpyxl
import xlwt
from xlwt import Workbook
import xlsxwriter

#Current
mintemparr=[]
hwaarr=[]
ab=[]
abresult=[]
elevation=[]
precipitationMAY=[]
avgtempfeb=[]
windapril=[]
maxtempaug=[]
BIO6=[]
BIO19=[]
BIO16=[]

#2021
minfebtemp2021B=[]
precipmay2021B=[]
maxaugtemp2021B=[]
BIO62021B=[]
BIO162021B=[]
BIO192021B=[]

#2041
minfebtemp2041B=[]
precipmay2041B=[]
maxaugtemp2041B=[]
BIO62041B=[]
BIO162041B=[]
BIO192041B=[]

#2061
minfebtemp2061B=[]
precipmay2061B=[]
maxaugtemp2061B=[]
BIO62061B=[]
BIO162061B=[]
BIO192061B=[]

#2081
minfebtemp2081B=[]
precipmay2081B=[]
maxaugtemp2081B=[]
BIO62081B=[]
BIO162081B=[]
BIO192081B=[]


counter=0
check=100
num=0
ender = 0

import pandas as pd
df = pd.DataFrame(columns=['Longitude', 'Latitude', 'Threat'])



def getmintemp ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/currentfeb.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        mintemparr.append(line.split(" "))
                count+=1

def getelevation ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/REALelevation.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-32768" not in line:
                        line=line.strip ()
                        elevation.append(line.split(" "))
                count+=1

def getprecipitationMAY ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/precipitationMAY.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-32768" not in line:
                        line=line.strip ()
                        precipitationMAY.append(line.split(" "))
                count+=1

def getavgtempfeb ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/avgtempfeb.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        avgtempfeb.append(line.split(" "))
                count+=1

def getwindapril ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/windapril.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        windapril.append(line.split(" "))
                count+=1

def getmaxtempaug ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/maxtempaug.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        maxtempaug.append(line.split(" "))
                count+=1

def getBIO6 ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/BIO6.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        BIO6.append(line.split(" "))
                count+=1

def getBIO19 ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/BIO19.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        BIO19.append(line.split(" "))
                count+=1

def getBIO16 ():
    count=0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/BIO16.txt', 'r', errors='ignore') as f:
            for line in f:
                if count%3==0:
                    if "-3.39999995214436425e+38" not in line:
                        line=line.strip ()
                        BIO16.append(line.split(" "))
                count+=1

def get2021minfebtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2021mintempfebWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    minfebtemp2021B.append(line.split(" "))
            count+=1

def get2021precipMAYB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2021precipMAYWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-32768" not in line:
                    line = line.strip()
                    precipmay2021B.append(line.split(" "))
            count+=1

def get2021maxaugtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2021maxtempAUGWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    maxaugtemp2021B.append(line.split(" "))
            count+=1

def get2021BIO6B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2021BIO6Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO62021B.append(line.split(" "))
            count+=1

def get2021BIO19B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2021BIO19Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO192021B.append(line.split(" "))
            count+=1

def get2021BIO16B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2021BIO16Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO162021B.append(line.split(" "))
            count+=1

def get2041minfebtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2041mintempfebWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    minfebtemp2041B.append(line.split(" "))
            count+=1

def get2041precipMAYB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2041precipMAYWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-32768" not in line:
                    line = line.strip()
                    precipmay2041B.append(line.split(" "))
            count+=1

def get2041maxaugtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2041maxtempAUGWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    maxaugtemp2041B.append(line.split(" "))
            count+=1

def get2041BIO6B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2041BIO6Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO62041B.append(line.split(" "))
            count+=1

def get2041BIO19B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2041BIO19Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO192041B.append(line.split(" "))
            count+=1

def get2041BIO16B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2041BIO16Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO162041B.append(line.split(" "))
            count+=1


def get2061minfebtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2061mintempfebWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    minfebtemp2061B.append(line.split(" "))
            count+=1

def get2061precipMAYB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2061precipMAYWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-32768" not in line:
                    line = line.strip()
                    precipmay2061B.append(line.split(" "))
            count+=1

def get2061maxaugtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2061maxtempAUGWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    maxaugtemp2061B.append(line.split(" "))
            count+=1

def get2061BIO6B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2061BIO6Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO62061B.append(line.split(" "))
            count+=1

def get2061BIO19B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2061BIO19Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO192061B.append(line.split(" "))
            count+=1

def get2061BIO16B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2061BIO16Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO162061B.append(line.split(" "))
            count+=1


def get2081minfebtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2081mintempfebWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    minfebtemp2081B.append(line.split(" "))
            count+=1

def get2081precipMAYB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2081precipMAYWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-32768" not in line:
                    line = line.strip()
                    precipmay2081B.append(line.split(" "))
            count+=1

def get2081maxaugtempB ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2081maxtempAUGWork.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    maxaugtemp2081B.append(line.split(" "))
            count+=1

def get2081BIO6B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2081BIO6Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO62081B.append(line.split(" "))
            count+=1

def get2081BIO19B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2081BIO19Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO192081B.append(line.split(" "))
            count+=1

def get2081BIO16B ():
    count = 0
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/2081BIO16Work.txt', 'r', errors='ignore') as f:
        for line in f:
            if count % 3 == 0:
                if "-3.39999995214436425e+38" not in line:
                    line = line.strip()
                    BIO162081B.append(line.split(" "))
            count+=1


def match (lon, lat):
    min=10000
    minindex=-1
    for x in range (len (mintemparr)):
        if (abs ((float (lon))-float (mintemparr [x][0])))+(abs ((float (lat))-float (mintemparr [x][1])))<min:
           min=(abs ((float (lon))-float (mintemparr [x][0])))+(abs ((float (lat))-float (mintemparr [x][1])))
           #print(min)
           minindex=x
    result=mintemparr [minindex][2]
    return result

def matchel (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (elevation)):
        if (abs ((float (lon))-float (elevation [x][0])))+(abs ((float (lat))-float (elevation [x][1])))<min:
           min=(abs ((float (lon))-float (elevation [x][0])))+(abs ((float (lat))-float (elevation [x][1])))
           #print(min)
           minindex=x
    result=elevation [minindex][2]
    return result

def matchprecipMAY (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (precipitationMAY)):
        if (abs ((float (lon))-float (precipitationMAY [x][0])))+(abs ((float (lat))-float (precipitationMAY [x][1])))<min:
           min=(abs ((float (lon))-float (precipitationMAY [x][0])))+(abs ((float (lat))-float (precipitationMAY [x][1])))
           #print(min)
           minindex=x
    result=precipitationMAY [minindex][2]
    return result

def matchavgtempfeb (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (avgtempfeb)):
        if (abs ((float (lon))-float (avgtempfeb [x][0])))+(abs ((float (lat))-float (avgtempfeb [x][1])))<min:
           min=(abs ((float (lon))-float (avgtempfeb [x][0])))+(abs ((float (lat))-float (avgtempfeb [x][1])))
           #print(min)
           minindex=x
    result=avgtempfeb [minindex][2]
    return result

def matchwindapril (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (windapril)):
        if (abs ((float (lon))-float (windapril [x][0])))+(abs ((float (lat))-float (windapril [x][1])))<min:
           min=(abs ((float (lon))-float (windapril [x][0])))+(abs ((float (lat))-float (windapril [x][1])))
           #print(min)
           minindex=x
    result=windapril [minindex][2]
    return result

def matchmaxtempaug (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (maxtempaug)):
        if (abs ((float (lon))-float (maxtempaug [x][0])))+(abs ((float (lat))-float (maxtempaug [x][1])))<min:
           min=(abs ((float (lon))-float (maxtempaug [x][0])))+(abs ((float (lat))-float (maxtempaug [x][1])))
           #print(min)
           minindex=x
    result=maxtempaug [minindex][2]
    return result

def matchBIO6 (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO6)):
        if (abs ((float (lon))-float (BIO6 [x][0])))+(abs ((float (lat))-float (BIO6 [x][1])))<min:
           min=(abs ((float (lon))-float (BIO6 [x][0])))+(abs ((float (lat))-float (BIO6 [x][1])))
           #print(min)
           minindex=x
    result=BIO6 [minindex][2]
    return result

def matchBIO19 (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO19)):
        if (abs ((float (lon))-float (BIO19 [x][0])))+(abs ((float (lat))-float (BIO19 [x][1])))<min:
           min=(abs ((float (lon))-float (BIO19 [x][0])))+(abs ((float (lat))-float (BIO19 [x][1])))
           #print(min)
           minindex=x
    result=BIO19 [minindex][2]
    return result

def matchBIO16 (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO16)):
        if (abs ((float (lon))-float (BIO16 [x][0])))+(abs ((float (lat))-float (BIO16 [x][1])))<min:
           min=(abs ((float (lon))-float (BIO16 [x][0])))+(abs ((float (lat))-float (BIO16 [x][1])))
           #print(min)
           minindex=x
    result=BIO16 [minindex][2]
    return result

def matchminfebtemp2021B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (minfebtemp2021B)):
        if (abs ((float (lon))-float (minfebtemp2021B [x][0])))+(abs ((float (lat))-float (minfebtemp2021B [x][1])))<min:
           min=(abs ((float (lon))-float (minfebtemp2021B [x][0])))+(abs ((float (lat))-float (minfebtemp2021B [x][1])))
           #print(min)
           minindex=x
    result=minfebtemp2021B [minindex][2]
    return result

def matchprecipMAY2021B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (precipmay2021B)):
        if (abs ((float (lon))-float (precipmay2021B [x][0])))+(abs ((float (lat))-float (precipmay2021B [x][1])))<min:
           min=(abs ((float (lon))-float (precipmay2021B [x][0])))+(abs ((float (lat))-float (precipmay2021B [x][1])))
           #print(min)
           minindex=x
    result=precipmay2021B [minindex][2]
    return result

def matchmaxtempAUG2021B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (maxaugtemp2021B)):
        if (abs ((float (lon))-float (maxaugtemp2021B [x][0])))+(abs ((float (lat))-float (maxaugtemp2021B [x][1])))<min:
           min=(abs ((float (lon))-float (maxaugtemp2021B [x][0])))+(abs ((float (lat))-float (maxaugtemp2021B [x][1])))
           #print(min)
           minindex=x
    result=maxaugtemp2021B [minindex][2]
    return result

def matchBIO62021B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO62021B)):
        if (abs ((float (lon))-float (BIO62021B [x][0])))+(abs ((float (lat))-float (BIO62021B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO62021B [x][0])))+(abs ((float (lat))-float (BIO62021B [x][1])))
           #print(min)
           minindex=x
    result=BIO62021B [minindex][2]
    return result

def matchBIO192021B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO192021B)):
        if (abs ((float (lon))-float (BIO192021B [x][0])))+(abs ((float (lat))-float (BIO192021B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO192021B [x][0])))+(abs ((float (lat))-float (BIO192021B [x][1])))
           #print(min)
           minindex=x
    result=BIO192021B [minindex][2]
    return result

def matchBIO162021B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO162021B)):
        if (abs ((float (lon))-float (BIO162021B [x][0])))+(abs ((float (lat))-float (BIO162021B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO162021B [x][0])))+(abs ((float (lat))-float (BIO162021B [x][1])))
           #print(min)
           minindex=x
    result=BIO162021B [minindex][2]
    return result


def matchminfebtemp2041B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (minfebtemp2041B)):
        if (abs ((float (lon))-float (minfebtemp2041B [x][0])))+(abs ((float (lat))-float (minfebtemp2041B [x][1])))<min:
           min=(abs ((float (lon))-float (minfebtemp2041B [x][0])))+(abs ((float (lat))-float (minfebtemp2041B [x][1])))
           #print(min)
           minindex=x
    result=minfebtemp2041B [minindex][2]
    return result

def matchprecipMAY2041B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (precipmay2041B)):
        if (abs ((float (lon))-float (precipmay2041B [x][0])))+(abs ((float (lat))-float (precipmay2041B [x][1])))<min:
           min=(abs ((float (lon))-float (precipmay2041B [x][0])))+(abs ((float (lat))-float (precipmay2041B [x][1])))
           #print(min)
           minindex=x
    result=precipmay2041B [minindex][2]
    return result

def matchmaxtempAUG2041B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (maxaugtemp2041B)):
        if (abs ((float (lon))-float (maxaugtemp2041B [x][0])))+(abs ((float (lat))-float (maxaugtemp2041B [x][1])))<min:
           min=(abs ((float (lon))-float (maxaugtemp2041B [x][0])))+(abs ((float (lat))-float (maxaugtemp2041B [x][1])))
           #print(min)
           minindex=x
    result=maxaugtemp2041B [minindex][2]
    return result

def matchBIO62041B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO62041B)):
        if (abs ((float (lon))-float (BIO62041B [x][0])))+(abs ((float (lat))-float (BIO62041B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO62041B [x][0])))+(abs ((float (lat))-float (BIO62041B [x][1])))
           #print(min)
           minindex=x
    result=BIO62041B [minindex][2]
    return result

def matchBIO192041B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO192041B)):
        if (abs ((float (lon))-float (BIO192041B [x][0])))+(abs ((float (lat))-float (BIO192041B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO192041B [x][0])))+(abs ((float (lat))-float (BIO192041B [x][1])))
           #print(min)
           minindex=x
    result=BIO192041B [minindex][2]
    return result

def matchBIO162041B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO162041B)):
        if (abs ((float (lon))-float (BIO162041B [x][0])))+(abs ((float (lat))-float (BIO162041B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO162041B [x][0])))+(abs ((float (lat))-float (BIO162041B [x][1])))
           #print(min)
           minindex=x
    result=BIO162041B [minindex][2]
    return result


def matchminfebtemp2061B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (minfebtemp2061B)):
        if (abs ((float (lon))-float (minfebtemp2061B [x][0])))+(abs ((float (lat))-float (minfebtemp2061B [x][1])))<min:
           min=(abs ((float (lon))-float (minfebtemp2061B [x][0])))+(abs ((float (lat))-float (minfebtemp2061B [x][1])))
           #print(min)
           minindex=x
    result=minfebtemp2061B [minindex][2]
    return result

def matchprecipMAY2061B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (precipmay2061B)):
        if (abs ((float (lon))-float (precipmay2061B [x][0])))+(abs ((float (lat))-float (precipmay2061B [x][1])))<min:
           min=(abs ((float (lon))-float (precipmay2061B [x][0])))+(abs ((float (lat))-float (precipmay2061B [x][1])))
           #print(min)
           minindex=x
    result=precipmay2061B [minindex][2]
    return result

def matchmaxtempAUG2061B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (maxaugtemp2061B)):
        if (abs ((float (lon))-float (maxaugtemp2061B [x][0])))+(abs ((float (lat))-float (maxaugtemp2061B [x][1])))<min:
           min=(abs ((float (lon))-float (maxaugtemp2061B [x][0])))+(abs ((float (lat))-float (maxaugtemp2061B [x][1])))
           #print(min)
           minindex=x
    result=maxaugtemp2061B [minindex][2]
    return result

def matchBIO62061B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO62061B)):
        if (abs ((float (lon))-float (BIO62061B [x][0])))+(abs ((float (lat))-float (BIO62061B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO62061B [x][0])))+(abs ((float (lat))-float (BIO62061B [x][1])))
           #print(min)
           minindex=x
    result=BIO62061B [minindex][2]
    return result

def matchBIO192061B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO192061B)):
        if (abs ((float (lon))-float (BIO192061B [x][0])))+(abs ((float (lat))-float (BIO192061B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO192061B [x][0])))+(abs ((float (lat))-float (BIO192061B [x][1])))
           #print(min)
           minindex=x
    result=BIO192061B [minindex][2]
    return result

def matchBIO162061B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO162061B)):
        if (abs ((float (lon))-float (BIO162061B [x][0])))+(abs ((float (lat))-float (BIO162061B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO162061B [x][0])))+(abs ((float (lat))-float (BIO162061B [x][1])))
           #print(min)
           minindex=x
    result=BIO162061B [minindex][2]
    return result


def matchminfebtemp2081B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (minfebtemp2081B)):
        if (abs ((float (lon))-float (minfebtemp2081B [x][0])))+(abs ((float (lat))-float (minfebtemp2081B [x][1])))<min:
           min=(abs ((float (lon))-float (minfebtemp2081B [x][0])))+(abs ((float (lat))-float (minfebtemp2081B [x][1])))
           #print(min)
           minindex=x
    result=minfebtemp2081B [minindex][2]
    return result

def matchprecipMAY2081B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (precipmay2081B)):
        if (abs ((float (lon))-float (precipmay2081B [x][0])))+(abs ((float (lat))-float (precipmay2081B [x][1])))<min:
           min=(abs ((float (lon))-float (precipmay2081B [x][0])))+(abs ((float (lat))-float (precipmay2081B [x][1])))
           #print(min)
           minindex=x
    result=precipmay2081B [minindex][2]
    return result

def matchmaxtempAUG2081B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (maxaugtemp2081B)):
        if (abs ((float (lon))-float (maxaugtemp2081B [x][0])))+(abs ((float (lat))-float (maxaugtemp2081B [x][1])))<min:
           min=(abs ((float (lon))-float (maxaugtemp2081B [x][0])))+(abs ((float (lat))-float (maxaugtemp2081B [x][1])))
           #print(min)
           minindex=x
    result=maxaugtemp2081B [minindex][2]
    return result

def matchBIO62081B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO62081B)):
        if (abs ((float (lon))-float (BIO62081B [x][0])))+(abs ((float (lat))-float (BIO62081B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO62081B [x][0])))+(abs ((float (lat))-float (BIO62081B [x][1])))
           #print(min)
           minindex=x
    result=BIO62081B [minindex][2]
    return result

def matchBIO192081B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO192081B)):
        if (abs ((float (lon))-float (BIO192081B [x][0])))+(abs ((float (lat))-float (BIO192081B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO192081B [x][0])))+(abs ((float (lat))-float (BIO192081B [x][1])))
           #print(min)
           minindex=x
    result=BIO192081B [minindex][2]
    return result

def matchBIO162081B (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO162081B)):
        if (abs ((float (lon))-float (BIO162081B [x][0])))+(abs ((float (lat))-float (BIO162081B [x][1])))<min:
           min=(abs ((float (lon))-float (BIO162081B [x][0])))+(abs ((float (lat))-float (BIO162081B [x][1])))
           #print(min)
           minindex=x
    result=BIO162081B [minindex][2]
    return result
def fillerandmatcher (ender):
    finalresult = []

    # Variable 1: Minimum Temperature
    if var1 == "1":
        if stringer == "1":
            if ender==0:
                getmintemp()
            mintemp = match(float(longitude), float(latitude))

        if stringer == "2":
            if ender==0:
                get2021minfebtempB()
            mintemp = matchminfebtemp2021B(float(longitude), float(latitude))

        if stringer == "3":
            if ender==0:
                get2041minfebtempB()
            mintemp = matchminfebtemp2041B(float(longitude), float(latitude))

        if stringer == "4":
            if ender == 0:
                get2061minfebtempB()
            mintemp = matchminfebtemp2061B(float(longitude), float(latitude))

        if stringer == "5":
            if ender == 0:
                get2081minfebtempB()
            mintemp = matchminfebtemp2081B(float(longitude), float(latitude))

        print(mintemp)
        finalresult.append(mintemp)

    # Variable 2: Elevation
    if var2 == "1":
        if ender == 0:
            getelevation()
        mintemp = matchel(float(longitude), float(latitude))
        print(mintemp)
        finalresult.append(mintemp)

    # Variable 3: Average Temperature
    if var3 == "1":
        if stringer == "1":
            if ender == 0:
                getavgtempfeb()
            average = matchprecipMAY(float(longitude), float(latitude))
            print(average)
            finalresult.append(average)

    # Variable 4: May Precipitation
    if var4 == "1":
        if stringer == "1":
            if ender == 0:
                getprecipitationMAY()
            precipMAY = matchprecipMAY(float(longitude), float(latitude))

        if stringer == "2":
            if ender == 0:
                get2021precipMAYB()
            precipMAY = matchprecipMAY2021B(float(longitude), float(latitude))

        if stringer == "3":
            if ender == 0:
                get2041precipMAYB()
            precipMAY = matchprecipMAY2041B(float(longitude), float(latitude))

        if stringer == "4":
            if ender == 0:
                get2061precipMAYB()
            precipMAY = matchprecipMAY2061B(float(longitude), float(latitude))

        if stringer == "5":
            if ender == 0:
                get2081precipMAYB()
            precipMAY = matchprecipMAY2081B(float(longitude), float(latitude))

        print(precipMAY)
        finalresult.append(precipMAY)

    # Variable 5: Wind April
    if var5 == "1":
        if stringer == "1":
            if ender == 0:
                getwindapril()
            wind = matchwindapril(float(longitude), float(latitude))
            print(wind)
            finalresult.append(wind)

    # Variable 6: Max temp
    if var6 == "1":
        if stringer == "1":
            if ender == 0:
                getmaxtempaug()
            maximumtempaug = matchmaxtempaug(float(longitude), float(latitude))

        if stringer == "2":
            if ender == 0:
                get2021maxaugtempB()
            maximumtempaug = matchmaxtempAUG2021B(float(longitude), float(latitude))

        if stringer == "3":
            if ender == 0:
                get2041maxaugtempB()
            maximumtempaug = matchmaxtempAUG2041B(float(longitude), float(latitude))

        if stringer == "4":
            if ender == 0:
                get2061maxaugtempB()
            maximumtempaug = matchmaxtempAUG2061B(float(longitude), float(latitude))

        if stringer == "5":
            if ender == 0:
                get2081maxaugtempB()
            maximumtempaug = matchmaxtempAUG2081B(float(longitude), float(latitude))

        print(maximumtempaug)
        finalresult.append(maximumtempaug)

    # Variable 7: BIO6
    if var7 == "1":
        if stringer == "1":
            if ender == 0:
                getBIO6()
            biolog6 = matchBIO6(float(longitude), float(latitude))

        if stringer == "2":
            if ender == 0:
                get2021BIO6B()
            biolog6 = matchBIO62021B(float(longitude), float(latitude))

        if stringer == "3":
            if ender == 0:
                get2041BIO6B()
            biolog6 = matchBIO62041B(float(longitude), float(latitude))

        if stringer == "4":
            if ender == 0:
                get2061BIO6B()
            biolog6 = matchBIO62061B(float(longitude), float(latitude))

        if stringer == "5":
            if ender == 0:
                get2081BIO6B()
            biolog6 = matchBIO62081B(float(longitude), float(latitude))

        print(biolog6)
        finalresult.append(biolog6)

    # Variable 8: BIO19
    if var8 == "1":
        if stringer == "1":
            if ender == 0:
                getBIO19()
            biolog19 = matchBIO19(float(longitude), float(latitude))

        if stringer == "2":
            if ender == 0:
                get2021BIO19B()
            biolog19 = matchBIO192021B(float(longitude), float(latitude))

        if stringer == "3":
            if ender == 0:
                get2041BIO19B()
            biolog19 = matchBIO192041B(float(longitude), float(latitude))

        if stringer == "4":
            if ender == 0:
                get2061BIO19B()
            biolog19 = matchBIO192061B(float(longitude), float(latitude))

        if stringer == "5":
            if ender == 0:
                get2081BIO19B()
            biolog19 = matchBIO192081B(float(longitude), float(latitude))

        print(biolog19)
        finalresult.append(biolog19)

    # Variable 9: BIO16
    if var9 == "1":
        if stringer == "1":
            if ender == 0:
                getBIO16()
            biolog16 = matchBIO16(float(longitude), float(latitude))

        if stringer == "2":
            if ender == 0:
                get2021BIO16B()
            biolog16 = matchBIO162021B(float(longitude), float(latitude))

        if stringer == "3":
            if ender == 0:
                get2041BIO16B()
            biolog16 = matchBIO162041B(float(longitude), float(latitude))

        if stringer == "4":
            if ender == 0:
                get2061BIO16B()
            biolog16 = matchBIO162061B(float(longitude), float(latitude))

        if stringer == "5":
            if ender == 0:
                get2081BIO16B()
            biolog16 = matchBIO162081B(float(longitude), float(latitude))

        print(biolog16)
        finalresult.append(biolog16)

    print(finalresult)
    return finalresult

def cleaner (dataset):
    if var1 == "2":
        dataset = dataset.drop('Min Temperature Feb', 1)
    if var2 == "2":
        dataset = dataset.drop('Elevation', 1)
    if var3 == "2":
        dataset = dataset.drop('Avg Temperature Feb', 1)
    if var4 == "2":
        dataset = dataset.drop('Precipitation May', 1)
    if var5 == "2":
        dataset = dataset.drop('Wind April', 1)
    if var6 == "2":
        dataset = dataset.drop('Max Temp Aug', 1)
    if var7 == "2":
        dataset = dataset.drop('BIO6', 1)
    if var8 == "2":
        dataset = dataset.drop('BIO19', 1)
    if var9 == "2":
        dataset = dataset.drop('BIO16', 1)

    print (dataset)
    return dataset


def RandomForests (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)
    dataset = cleaner(dataset)
    # dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
    print(dataset.head())
    print(varnum)
    X = dataset.iloc[:, 0: varnum].values
    y = dataset.iloc[:, varnum].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    # print(X_train)

    from sklearn.ensemble import RandomForestClassifier

    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    if varnum == 1:
        pred = [[array[0]]]
    if varnum == 2:
        pred = [[array[0], array[1]]]
    if varnum == 3:
        pred = [[array[0], array[1], array[2]]]
    if varnum == 4:
        pred = [[array[0], array[1], array[2], array[3]]]
    if varnum == 5:
        pred = [[array[0], array[1], array[2], array[3], array[4]]]
    if varnum == 6:
        pred = [[array[0], array[1], array[2], array[3], array[4], array[5]]]
    if varnum == 7:
        pred = [[array[0], array[1], array[2], array[3], array[4], array[5], array[6]]]
    if varnum == 8:
        pred = [[array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7]]]
    if varnum == 9:
        pred = [[array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8]]]

    finalpred = classifier.predict(pred)
    thepred = classifier.predict_proba(pred)

    print(finalpred)
    print(thepred)

    y_pred = classifier.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    #from matplotlib import pyplot

    #importance = classifier.feature_importances_

    #for i, v in enumerate(importance):
        #print('Feature: %0d, Score: %.5f' % (i, v))

    #pyplot.bar([x for x in range(len(importance))], importance)
    #pyplot.show()

    newarr = thepred[0]
    return float (newarr [1])



def present (longitude, latitude):
    if len (mintemparr)==0:
        print ("welcome to filler")
        getmintemp()
        getelevation()
        getprecipitationMAY()
        getavgtempfeb()
        getwindapril()
        getmaxtempaug()
        getBIO6()
        getBIO19()
        getBIO16()

    mintemp = match(float(longitude), float(latitude))
    print(mintemp)
    el = matchel(float(longitude), float(latitude))
    print(el)
    precipMAY = matchprecipMAY(float(longitude), float(latitude))
    print(precipMAY)
    average = matchavgtempfeb(float(longitude), float(latitude))
    print(average)
    wind = matchwindapril(float(longitude), float(latitude))
    print(wind)
    maximumtempaug = matchmaxtempaug(float(longitude), float(latitude))
    print(maximumtempaug)
    biolog6 = matchBIO6(float(longitude), float(latitude))
    print(biolog6)
    biolog19 = matchBIO19(float(longitude), float(latitude))
    print(biolog19)
    biolog16 = matchBIO16(float(longitude), float(latitude))
    print(biolog16)

    finalresult = []
    finalresult.append(mintemp)
    finalresult.append(el)
    finalresult.append(average)
    finalresult.append(precipMAY)
    finalresult.append(wind)
    finalresult.append(maximumtempaug)
    finalresult.append(biolog6)
    finalresult.append(biolog19)
    finalresult.append(biolog16)
    return finalresult

def MYSQLSPEED (year, longitude, latitude):

    try:
        connection = mysql.connector.connect(host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
                                             user="admin",
                                             password="findyourinvasive",
                                             database="findyourinvasivedev")

        if year=="1":
            sql_select_Query = "select * from 001a"
        elif year=="3":
            print ("helloavi")
            sql_select_Query = "select * from 0012041a"
        elif year=="4":
            sql_select_Query = "select * from 0012061a"
        elif year=="5":
            sql_select_Query = "select * from 0012081a"
        else:
            return -1


        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        print("\nPrinting each invasive record")
        longi=[]
        lat=[]
        threat=[]
        for row in records:
            longi.append (row[0])
            lat.append (row[1])
            threat.append (row[2])

        for x in range (len (longi)):
                if (abs (float (longitude)-float (longi[x])))+(abs (float (latitude)-float (lat[x])))<1.5:
                    if (connection.is_connected()):
                        connection.close()
                        cursor.close()
                        print("MySQL connection is closed")
                        return threat [x]
        return -1


    except Error as e:
        print("Error reading data from MySQL table", e)
        return -1

def MYSQLADD (code, lon, lat, ab):
    print ("welcome to add")
    print ("this is lon"+str (lon))
    print ("this is lat"+str (lat))
    print ("this is ab"+str (ab))
    mydb = mysql.connector.connect(
        host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
        user="admin",
        password="findyourinvasive",
        database="findyourinvasivedev"
    )

    finalres=present(lon,lat)

    print(finalres)

    for x in range(len(finalres)):  # Trying to truncate

        if len(finalres[x]) > 6:
            finalres[x] = finalres[x][0:6]

        finalres[x] = float(finalres[x])

    if ab==1:
        finalres.append(1.0)
    elif ab==0:
        finalres.append (0.0)

    print (finalres)

    mycursor = mydb.cursor()

    sql = "INSERT INTO 2var"+code+"a VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (finalres [0], finalres [1], finalres [2], finalres [3], finalres [4], finalres [5],
                                                                                        finalres [6], finalres [7], finalres [8], finalres [9])

    sql3= "INSERT INTO justlatlon"+code+"a VALUES (%s, %s)", (lon, lat)
    mycursor.execute(*sql)
    mycursor.execute(*sql3)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return

def MYSQLAbCheck (code,longitude, latitude):
    connection = mysql.connector.connect(host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
                                         user="admin",
                                         password="findyourinvasive",
                                         database="findyourinvasivedev")


    sql_select_Query = "select * from justlatlon"+code+"a"

    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    longi = []
    lat = []

    for row in records:
        longi.append(row[0])
        lat.append(row[1])

    for x in range(len(longi)):
        if (abs(float(longitude) - float(longi[x]))) + (abs(float(latitude) - float(lat[x]))) < 0.5:
                return -1


def Create2varTable (code):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
        user="admin",
        password="findyourinvasive",
        database="findyourinvasivedev"
    )

    mycursor = mydb.cursor()

    name="2var"+code+"a"

    sql = "CREATE TABLE IF NOT EXISTS "+ name + """(mtf FLOAT(10,7), el FLOAT(10,7), atf FLOAT(10,7), pm FLOAT(10,7), wa FLOAT(10,7), mta FLOAT(10,7), b6 FLOAT(10,7), b19 FLOAT(10,7), b16 FLOAT(10,7), p FLOAT(10,7))"""

    mycursor.execute(sql)

    print ("Done")


def CreatejustlatlonTable (code):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
        user="admin",
        password="findyourinvasive",
        database="findyourinvasivedev"
    )

    mycursor = mydb.cursor()

    name = "justlatlon" + code + "a"
    sql = "CREATE TABLE IF NOT EXISTS "+name+ """(Longitude FLOAT(10,7), Latitude FLOAT(10,7))"""

    mycursor.execute(sql)

    print ("Done")

def Neural (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)
    dataset = cleaner(dataset)
    # dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
    print(dataset.head())
    print(varnum)
    X = dataset.iloc[:, 0: varnum].values
    y = dataset.iloc[:, varnum].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    mlp.fit(X_train, y_train.ravel())

    predictions = mlp.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    if varnum == 1:
        pred = [[float (array[0])]]
    if varnum == 2:
        pred = [[float (array[0]), float (array[1])]]
    if varnum == 3:
        pred = [[float (array[0]), float (array[1]), float (array[2])]]
    if varnum == 4:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3])]]
    if varnum == 5:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4])]]
    if varnum == 6:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5])]]
    if varnum == 7:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6])]]
    if varnum == 8:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7])]]
    if varnum == 9:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7]), float (array[8])]]

    finalpred = mlp.predict(pred)
    thepred = mlp.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, predictions))
    newarr = thepred[0]
    print (newarr)
    return float (newarr [1])


def Linear (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)
    dataset = cleaner(dataset)
    # dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
    print(dataset.head())
    print(varnum)
    X = dataset.iloc[:, 0: varnum].values
    y = dataset.iloc[:, varnum].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    if varnum == 1:
        pred = [[float (array[0])]]
    if varnum == 2:
        pred = [[float (array[0]), float (array[1])]]
    if varnum == 3:
        pred = [[float (array[0]), float (array[1]), float (array[2])]]
    if varnum == 4:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3])]]
    if varnum == 5:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4])]]
    if varnum == 6:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5])]]
    if varnum == 7:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6])]]
    if varnum == 8:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7])]]
    if varnum == 9:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7]), float (array[8])]]

    finalpred = regressor.predict(pred)
    #thepred = regressor.predict_proba(pred)
    print(finalpred)
    #print(thepred)
    #from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    #print(accuracy_score(y_test, y_pred))
    #newarr = thepred[0]
    #print (newarr)
    finalpred = float(finalpred)
    if finalpred < 0:
        finalpred = 0
    return finalpred



def Logit (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)
    dataset = cleaner(dataset)
    # dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
    print(dataset.head())
    print(varnum)
    X = dataset.iloc[:, 0: varnum].values
    y = dataset.iloc[:, varnum].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    from sklearn.linear_model import LogisticRegression

    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    if varnum == 1:
        pred = [[float (array[0])]]
    if varnum == 2:
        pred = [[float (array[0]), float (array[1])]]
    if varnum == 3:
        pred = [[float (array[0]), float (array[1]), float (array[2])]]
    if varnum == 4:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3])]]
    if varnum == 5:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4])]]
    if varnum == 6:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5])]]
    if varnum == 7:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6])]]
    if varnum == 8:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7])]]
    if varnum == 9:
        pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7]), float (array[8])]]

    finalpred = regressor.predict(pred)
    #thepred = regressor.predict_proba(pred)
    print(finalpred)
    #print(thepred)
    #from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    #print(accuracy_score(y_test, y_pred))
    #newarr = thepred[0]
    #print (newarr)
    finalpred = float(finalpred)
    if finalpred < 0:
        finalpred = 0
    return finalpred


def ExtraModel (longitude, latitude):
    print ("This is ender"+ str (ender))

    def addrow (longitude, latitude, threat):
        print ("Welcome to add row")
        from numpy.random import randint
        arr32=[]
        arr32.append (longitude)
        arr32.append (latitude)
        arr32.append (threat)
        #df.loc [ender]=arr32
        df_length = len(df)
        df.loc[df_length] = arr32
        print (df)
        print ("Row sucessfully added")



    if model=="1":
        finalresult=fillerandmatcher(ender)

        print ("Welcome to the model")
        thepred=RandomForests(finalresult, codeval)

        #doublearray = thepred[0]
        #yesfinal = str(doublearray[1])

        addrow(longitude, latitude, thepred)




    if model=="2" or model=="3" or model=="4" or model=="5":

        finalresult=fillerandmatcher(ender)

        if model == "2":
            thepred=Neural(finalresult, codeval)
            #doublearray = thepred[0]
            #yesfinal = str(doublearray[1])
            addrow(longitude, latitude, thepred)



        elif model == "3":

            thepred=Linear(finalresult, codeval)
            #doublearray = thepred[0]
            #yesfinal = str(doublearray[1])
            addrow(longitude, latitude, thepred)



        elif model == "4":

            thepred=Logit(finalresult, codeval)
            #doublearray = thepred[0]
            #yesfinal = str(doublearray[1])
            addrow(longitude, latitude, thepred)

    return



def ArcGisMapper (codeval):
    print ("Welcome to ArcGIS")
    from arcgis.gis import GIS
    import pandas as pd
    import json
    import pymysql
    import pandas
    import random
    import string
    name = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    name=str (name)
    filename="C:/Users/aviba/PycharmProjects/colors/Map/"+name+".csv"
    print (filename)
    df.to_csv(filename, index=False)
    print (filename)

    g = GIS("https://www.arcgis.com", "findyourinvasive3299", "aviayaan321")
    title=str (codeval)+name
    p = {
        'type': "CSV",
        'title': title,
        'snippet': 'hwa',
        'description': 'test ' + \
                       'dataframe object to a GIS item',
        'tags': 'python',

    }

    i = g.content.add(item_properties=p,
                      data="C:/Users/aviba/PycharmProjects/colors/Map/"+name+".csv"
                      )
    q = i.publish()
    print(q)
    search = g.content.search(title, item_type="Feature Layer")
    print(search)
    from arcgis.mapping import WebMap
    map = WebMap()
    #map = g.map(location="United States")
    item = search[0]
    print(item)
    map.add_layer(item)
    props = {'title': title,
             'snippet': 'hwa',
             'tags': 'python',
             "renderer": "autocast",
             "field_name": "Threat",
             }
    map.save(props)
    import time
    time.sleep(5)

    map_id = g.content.search(title, item_type='Web Map')[0].id
    print(map_id)
    g.content.search(title, item_type='Web Map')[0].share(everyone=True)
    g.content.search(title, item_type='Feature Layer')[0].share(everyone=True)
    g.content.search(title, item_type='CSV')[0].share(everyone=True)

    import os
    os.remove("C:/Users/aviba/PycharmProjects/colors/Map/"+name+".csv")

    # map.export_to_html("filer.txt")

    # map.("C:/Users/aviba/PycharmProjects/colors/Map/html4.txt")

    return map_id

#Questions
feature= input ("Type 1 for Invasive Tracker, Type 2 for Add Your Invasive, Type 3 for Create Your Invasive:, Type 4 for Map: ")
if feature=="1" or feature=="4":
    model=input ("Type 1 for Random Forests, 2 for neural network, 3 for linear regression, 4 for logisitc regression, 5 for combo: ")
    stringer=input ("Type 1 for current, type 2 for 2021-2040, type 3 for 2041-2060, type 4 for 2061-2080, type 5 for 2081-2100: ")
    if feature=="1":
        auto=input ("Press 1 for Manual or Press 2 for Automatic: ")
        if auto=="2":
            longitude = input("Enter Longitude: ")
            latitude = input("Enter Latitude: ")
else:
    model=""
    stringer=""
    longitude=""
    latitude=""
    auto=""

if feature!="2":
    codeval=input ("Type in invasive code (See Documentation): ")

#End of Questions

#Fast calculation (only for HWA)
if feature=="4":

    countspecial = input("How many times do you want to run the model?")
    countspecial = int(countspecial)
    countspecial -= 1
    maptype = input("Type 1 for US, 2 for World: ")

    while ender <= countspecial:

        if maptype == "1":
            region=input ("Select a region: "
                          "Type 1 for general US, type 2 for Northeast,"
                          "type 3 for Southeast, type 4 for MidWest"
                          "type 5 for West, type 6 for SouthWest, "
                          "Type 7 for New York")
            if region=="1":
                longitude = str(random.randint(-124, -67))
                latitude = str(random.randint(25, 48))

            if region=="2":
                longitude = str(random.randint(-79, -69))
                latitude = str(random.randint(39, 45))

            if region=="3":
                longitude = str(random.randint(-88, -75))
                latitude = str(random.randint(27, 38))

            if region=="4":
                longitude = str(random.randint(-103, -84))
                latitude = str(random.randint(36, 48))

            if region=="5":
                longitude = str(random.randint(-124, -105))
                latitude = str(random.randint(35, 48))

            if region=="6":
                longitude = str(random.randint(-114, -102))
                latitude = str(random.randint(31, 40))

            if region=="7":
                longitude = str(random.randint(-78, -73))
                latitude = str(random.randint(40, 44))


        elif  maptype == "2":
            longitude = str(random.randint(-180, 180))
            latitude = str(random.randint(-90, 90))
        print(latitude)
        print(longitude)
        ExtraModel(longitude, latitude)
        ender += 1
    identification=ArcGisMapper(codeval)
    print (identification)


if feature=="1" and codeval=="001" and model=="1":

    print ("Proceed to Speed")
    res=MYSQLSPEED(stringer,longitude,latitude)
    if res==-1:
        print ("No Matches")
    else:
        print (res)


if feature=="1":
    manualarr=[]
    varnum = 0
    var1 = input("1 On or 2 Off")
    if var1 == "1":
        if auto=="1":
            mintemp = input("Type in minimum february temperature in degrees C: ")
            manualarr.append (mintemp)
        varnum += 1

    var2 = input("1 On or 2 Off")
    if var2 == "1":
        if auto=="1":
            el=input ("Type in  elevation in m: ")
            manualarr.append(el)
        varnum += 1

    if stringer=="1":
        var3 = input("1 On or 2 Off")
        if var3 == "1":
            if auto == "1":
                precipMAY=input ("Type in precipitation in May in mm: ")
                manualarr.append(precipMAY)
            varnum += 1
    else:
        var3="2"

    var4 = input("1 On or 2 Off")
    if var4 == "1":
        if auto == "1":
            average=input ("Type in average feburary temperature in degrees C: ")
            manualarr.append(average)
        varnum += 1

    if stringer=="1":
        var5 = input("1 On or 2 Off")
        if var5 == "1":
            if auto == "1":
                wind=input ("Type in wind speed in m s^-1: ")
                manualarr.append(wind)
            varnum += 1
    else:
        var5="2"

    var6 = input("1 On or 2 Off")
    if var6 == "1":
        if auto == "1":
            maximumtempaug=input ("Type in maximum temperature in august in degrees C: ")
            manualarr.append(maxtempaug)
        varnum += 1

    var7 = input("1 On or 2 Off")
    if var7 == "1":
        if auto == "1":
            biolog6=input ("Type in Min Temperature of Coldest Month in degrees C: ")
            manualarr.append(biolog6)
        varnum += 1

    var8 = input("1 On or 2 Off")
    if var8 == "1":
        if auto == "1":
            biolog19 = input("Type in Precipitation of Coldest Quarter in mm: ")
            manualarr.append(biolog19)
        varnum += 1
    var9 = input("1 On or 2 Off")
    if var9 == "1":
        if auto == "1":
            biolog16=input ("Type in Precipitation of Wettest Quarter in mm: ")
            manualarr.append(biolog16)
        varnum += 1


    if model=="1":

        if auto=="2":

            finalresult=fillerandmatcher (0)
            RandomForests(finalresult, codeval)
        else:
            RandomForests(manualarr, codeval)


    if model=="2" or model=="3" or model=="4" or model=="5":
        stats = []
        if auto=="2":
            finalresult=fillerandmatcher(0)
        else:
            finalresult=manualarr

        if model == "2":
            Neural(finalresult, codeval)
        elif model == "3":
            Linear(finalresult, codeval)
        elif model == "4":
            Logit(finalresult, codeval)
        elif model == "5":
            a=Neural(finalresult, codeval)
            b=Linear(finalresult, codeval)
            c=Logit(finalresult, codeval)
            d=RandomForests(finalresult, codeval)
            a=float (a)
            b=float (b)
            c=float (c)
            d=float (d)
            stats.append (a)
            stats.append (b)
            stats.append (c)
            stats.append (d)

            import statistics

            sd = statistics.stdev(stats)
            mean = statistics.mean(stats)

            print(sd)
            print(mean)

            for x in range(len(stats)):
                if float (stats[x]) > (float (mean) + 2 * float (sd)) or float (stats[x]) < (float (mean) - 2 * float (sd)):
                    print("We will delete this entry: " + stats[x])
                    stats.remove(stats[x])

            print("All clear")
            newmean = statistics.mean(stats)
            print(newmean)


elif feature == "2":
    #invasivenums="33343363423624233334"
    invasivenums = "334"
    codes=["20","21","22"]
    for y in range (len (invasivenums)):
        region=invasivenums [y:y+1]
        currentcode=codes [y]
        for x in range (5):
            if region == "1":
                longitude = str(random.randint(-124, -67))
                latitude = str(random.randint(25, 48))

            if region == "2":
                longitude = str(random.randint(-79, -69))
                latitude = str(random.randint(39, 45))

            if region == "3":
                longitude = str(random.randint(-88, -75))
                latitude = str(random.randint(27, 38))

            if region == "4":
                longitude = str(random.randint(-103, -84))
                latitude = str(random.randint(36, 48))

            if region == "5":
                longitude = str(random.randint(-124, -105))
                latitude = str(random.randint(35, 48))

            if region == "6":
                longitude = str(random.randint(-114, -102))
                latitude = str(random.randint(31, 40))

            if region == "7":
                longitude = str(random.randint(-78, -73))
                latitude = str(random.randint(40, 44))

            plon=random.randint(-124, -67)
            plat=random.randint(24, 48)

            MYSQLADD (currentcode, longitude, latitude, 1)

            while MYSQLAbCheck(currentcode,plon, plat)==-1:
                print ("welcome to ab generator")
                plon = random.randint(-124, -67)
                plat = random.randint(24, 48)

            print (plon)
            print (plat)
            print ("going to add ab now")
            MYSQLADD (currentcode, plon, plat, 0)

elif feature=="3":
    from csv import reader
    with open('InvasiveListFinal.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            print(row)
            print (row [0])
            Create2varTable (row [0])
            CreatejustlatlonTable (row [0])


    #mydb = mysql.connector.connect(
        #host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
        #user="admin",
        #password="findyourinvasive",
        #database="findyourinvasivedev"
    #)
    #cursor = mydb.cursor()

    #cursor.close()
    #mydb.close()

    #print("MySQL connection is closed")

    print ("Done")
