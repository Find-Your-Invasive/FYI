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
futurenum=0



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


def RandomForests (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM '+name, con=db_connection)

    #dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
    print(dataset.head())
    X = dataset.iloc[:, 0:9].values
    y = dataset.iloc[:, 9].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    #print(X_train)

    from sklearn.ensemble import RandomForestClassifier

    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    pred = [[array [0], array [1], array [2], array [3], array [4], array [5], array [6], array [7], array [8]]]
    finalpred = classifier.predict(pred)
    thepred = classifier.predict_proba(pred)

    print(finalpred)
    print(thepred)

    y_pred = classifier.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    from matplotlib import pyplot

    importance = classifier.feature_importances_

    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))

    pyplot.bar([x for x in range(len(importance))], importance)
    pyplot.show()

    newarr = thepred[0]
    return float (newarr [1])

def RandomForestsEAB (array):
    import pandas as pd
    import numpy as np
    dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/PrescenceANDAbscence.csv")
    print(dataset.head())
    X = dataset.iloc[:, 0:9].values
    y = dataset.iloc[:, 9].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    #print(X_train)

    from sklearn.ensemble import RandomForestClassifier

    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    pred = [[array [0], array [1], array [2], array [3], array [4], array [5], array [6], array [7], array [8]]]
    finalpred = classifier.predict(pred)
    thepred = classifier.predict_proba(pred)

    print(finalpred)
    print(thepred)

    y_pred = classifier.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    print(accuracy_score(y_test, y_pred))

    from matplotlib import pyplot

    importance = classifier.feature_importances_

    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))

    pyplot.bar([x for x in range(len(importance))], importance)
    pyplot.show()

    return



def futureRandomForests (array, code):
    import pandas as pd
    import numpy as np
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd


    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "future2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)

    #dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/future2var.csv")
    print(dataset.head())
    X = dataset.iloc[:, 0:7].values
    y = dataset.iloc[:, 7].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    # print(X_train)

    from sklearn.ensemble import RandomForestClassifier

    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    #y_pred = classifier.predict(X_test)

    #from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    #print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))
    #print(accuracy_score(y_test, y_pred))

    from matplotlib import pyplot

    importance = classifier.feature_importances_

    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))

    pyplot.bar([x for x in range(len(importance))], importance)
    pyplot.show()

    pred = [[array[0], array[1], array[2], array[3], array[4], array[5], array[6]]]
    finalpred = classifier.predict(pred)
    thepred = classifier.predict_proba(pred)
    print(finalpred)
    print(thepred)

    return thepred
    #newarr = thepred[0]
    #print (newarr)
    #return float (newarr [1])

def futureRandomForestsEAB (array):
    import pandas as pd
    import numpy as np

    dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/PrescenceANDAbscenceFuture.csv")
    print(dataset.head())
    X = dataset.iloc[:, 0:7].values
    y = dataset.iloc[:, 7].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
    # print(X_train)

    from sklearn.ensemble import RandomForestClassifier

    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    #y_pred = classifier.predict(X_test)

    #from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    #print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))
    #print(accuracy_score(y_test, y_pred))

    from matplotlib import pyplot

    importance = classifier.feature_importances_

    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))

    pyplot.bar([x for x in range(len(importance))], importance)
    pyplot.show()

    pred = [[array[0], array[1], array[2], array[3], array[4], array[5], array[6]]]
    finalpred = classifier.predict(pred)
    thepred = classifier.predict_proba(pred)
    print(finalpred)
    print(thepred)

    return thepred

def present (longitude, latitude):
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
    sql2 = "INSERT INTO future2var"+code+"a VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (finalres [0], finalres [1], finalres [3], finalres [5], finalres [6], finalres [7],
                                                                                       finalres [8], finalres [9])
    sql3= "INSERT INTO justlatlon"+code+"a VALUES (%s, %s)", (lon, lat)
    mycursor.execute(*sql)
    mycursor.execute(*sql2)
    mycursor.execute(*sql3)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def MYSQLAbCheck (code,longitude, latitude):
    connection = mysql.connector.connect(host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
                                         user="admin",
                                         password="findyourinvasive",
                                         database="findyourinvasivedev")


    sql_select_Query = "select * from justlatlon"+code+"001a"

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

def Create2varFutureTable (code):
    import mysql.connector

    mydb = mysql.connector.connect(
        host="fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com",
        user="admin",
        password="findyourinvasive",
        database="findyourinvasivedev"
    )

    mycursor = mydb.cursor()

    name = "future2var" + code + "a"

    sql = "CREATE TABLE IF NOT EXISTS " + name + """(mtf FLOAT(10,7), el FLOAT(10,7), pm FLOAT(10,7), mta FLOAT(10,7), b6 FLOAT(10,7), b19 FLOAT(10,7), b16 FLOAT(10,7), p FLOAT(10,7))"""

    mycursor.execute(sql)

    print("Done")

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

    print(dataset.head())
    X = dataset.iloc[:, 0:9]
    y = dataset.iloc[:, 9]
    print (y.head ())

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    mlp.fit(X_train, y_train.values.ravel())

    predictions = mlp.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7]), float (array[8])]]
    finalpred = mlp.predict(pred)
    thepred = mlp.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, predictions))

    return thepred
    #newarr = thepred[0]
    #print (newarr)
    #return float (newarr [1])

def futureNeural (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd
    import numpy as np
    #array = array.astype(np.float64)

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "future2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)

    print(dataset.head())
    X = dataset.iloc[:, 0:7]
    y = dataset.iloc[:, 7]
    print (y.head ())

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neural_network import MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
    mlp.fit(X_train, y_train.values.ravel())

    predictions = mlp.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))

    pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6])]]

    finalpred = mlp.predict(pred)

    thepred = mlp.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, predictions))

    return thepred

    #newarr = thepred[0]
    #print (newarr)
    #return float (newarr [1])

def Linear (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)

    print(dataset.head())
    X = dataset.iloc[:, 0:9]
    y = dataset.iloc[:, 9]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7]), float (array[8])]]
    finalpred = regressor.predict(pred)
    thepred = regressor.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, y_pred))

    return thepred
    #newarr = thepred[0]
    #print (newarr)
    #return float (newarr [1])

def futureLinear (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "future2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)

    print(dataset.head())
    X = dataset.iloc[:, 0:7]
    y = dataset.iloc[:, 7]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6])]]
    finalpred = regressor.predict(pred)
    thepred = regressor.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, y_pred))

    return thepred
    #newarr = thepred[0]
    #print (newarr)
    #return float (newarr [1])


def Logit (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)

    print(dataset.head())
    X = dataset.iloc[:, 0:9]
    y = dataset.iloc[:, 9]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    from sklearn.linear_model import LogisticRegression

    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6]), float (array[7]), float (array[8])]]
    finalpred = regressor.predict(pred)
    thepred = regressor.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, y_pred))

    return thepred
    #newarr = thepred[0]
    #print (newarr)
    #return float (newarr [1])

def futureLogit (array, code):
    from sqlalchemy import create_engine
    import pymysql
    import pandas as pd

    db_connection_str = 'mysql+pymysql://admin:findyourinvasive@fyidev.cj4ghwejxvaa.us-east-2.rds.amazonaws.com/findyourinvasivedev'
    db_connection = create_engine(db_connection_str)

    name = "future2var" + code + "a"
    dataset = pd.read_sql('SELECT * FROM ' + name, con=db_connection)

    print(dataset.head())
    X = dataset.iloc[:, 0:7]
    y = dataset.iloc[:, 7]

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    from sklearn.linear_model import LogisticRegression

    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    pred = [[float (array[0]), float (array[1]), float (array[2]), float (array[3]), float (array[4]), float (array[5]), float (array[6])]]
    finalpred = regressor.predict(pred)
    thepred = regressor.predict_proba(pred)
    print(finalpred)
    print(thepred)
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print(accuracy_score(y_test, y_pred))

    return thepred
    #newarr=thepred [0]
    #print (newarr)
    #return float (newarr [1])

#Questions

model=input ("Type 1 for Random Forests, 2 for neural network, 3 for linear regression, 4 for logisitc regression: ")
stringer=input ("Type 1 for current, type 2 for 2021-2040, type 3 for 2041-2060, type 4 for 2061-2080, type 5 for 2081-2100: ")
codeval=input ("Type in invasive code (See Documentation): ")
maptype=input ("Type 1 for US, 2 for World: ")

ender=0
count=""
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

countspecial= input ("How many times do you want to run the model?")
countspecial=int (countspecial)
countspecial-=1

#End of Questions

while ender<=countspecial:
    ender+=1

    if maptype=="1":
        longitude = str(random.randint(-124, -67))
        latitude = str(random.randint(25, 48))
    elif maptype=="2":
        longitude = str(random.randint(-180, 180))
        latitude = str(random.randint(-90, 90))

    print (latitude)
    print (longitude)

    #Fast calculation (only for HWA)
    if codeval=="001" and model=="1":

        print ("Proceed to Speed")
        res=MYSQLSPEED(stringer,longitude,latitude)
        if res==-1:
            print ("No Matches")
        else:
            print (res)


    if model=="1":
        if stringer=="1":
            if ender==1:
                getmintemp ()
                getelevation ()
                getprecipitationMAY ()
                getavgtempfeb ()
                getwindapril ()
                getmaxtempaug ()
                getBIO6 ()
                getBIO19 ()
                getBIO16 ()

            mintemp=match (float (longitude) , float (latitude))
            print (mintemp)
            el=matchel (float (longitude) , float (latitude))
            print (el)
            precipMAY=matchprecipMAY (float (longitude) , float (latitude))
            print (precipMAY)
            average=matchavgtempfeb (float (longitude) , float (latitude))
            print (average)
            wind=matchwindapril (float (longitude) , float (latitude))
            print (wind)
            maximumtempaug=matchmaxtempaug (float (longitude) , float (latitude))
            print (maximumtempaug)
            biolog6=matchBIO6 (float (longitude) , float (latitude))
            print (biolog6)
            biolog19=matchBIO19 (float (longitude) , float (latitude))
            print (biolog19)
            biolog16=matchBIO16 (float (longitude) , float (latitude))
            print (biolog16)

            finalresult=[]
            finalresult.append (mintemp)
            finalresult.append (el)
            finalresult.append (average)
            finalresult.append (precipMAY)
            finalresult.append(wind)
            finalresult.append (maximumtempaug)
            finalresult.append (biolog6)
            finalresult.append (biolog19)
            finalresult.append (biolog16)
            print (finalresult)

        elif stringer=="2":
            if ender==1:
                get2021minfebtempB()
                get2021precipMAYB()
                get2021maxaugtempB()
                getelevation()
                get2021BIO6B()
                get2021BIO19B()
                get2021BIO16B()

            mintemp = matchminfebtemp2021B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2021B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2021B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62021B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192021B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162021B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        elif stringer=="3":
            if ender==1:
                get2041minfebtempB()
                get2041precipMAYB()
                get2041maxaugtempB()
                getelevation()
                get2041BIO6B()
                get2041BIO19B()
                get2041BIO16B()

            mintemp = matchminfebtemp2041B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2041B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2041B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62041B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192041B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162041B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        elif stringer=="4":
            if ender==1:
                get2061minfebtempB()
                get2061precipMAYB()
                get2061maxaugtempB()
                getelevation()
                get2061BIO6B()
                get2061BIO19B()
                get2061BIO16B()

            mintemp = matchminfebtemp2061B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2061B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2061B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62061B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192061B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162061B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        elif stringer=="5":
            if ender==1:
                get2081minfebtempB()
                get2081precipMAYB()
                get2081maxaugtempB()
                getelevation()
                get2081BIO6B()
                get2081BIO19B()
                get2081BIO16B()

            mintemp = matchminfebtemp2081B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2081B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2081B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62081B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192081B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162081B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)


        if stringer=="1":
            while ender<=countspecial:
                thepred=RandomForests(finalresult, codeval)

                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

        if stringer!="1":
            while ender<=countspecial:
                thepred=futureRandomForests(finalresult, codeval)

                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

    if model=="2" or model=="3" or model=="4" or model=="5":
        stats = []

        if stringer=="1":
            if ender==1:
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
            print(finalresult)

        if stringer=="2":
            if ender == 1:
                get2021minfebtempB()
                getelevation()
                get2021precipMAYB()
                get2021maxaugtempB()
                get2021BIO6B()
                get2021BIO19B()
                get2021BIO16B()

            mintemp = matchminfebtemp2021B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2021B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2021B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62021B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192021B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162021B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        if stringer=="3":
            if ender == 1:
                get2041minfebtempB()
                getelevation()
                get2041precipMAYB()
                get2041maxaugtempB()
                get2021BIO6B()
                get2021BIO19B()
                get2021BIO16B()

            mintemp = matchminfebtemp2041B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2041B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2041B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62041B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192041B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162041B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        if stringer=="4":
            if ender == 1:
                get2061minfebtempB()
                getelevation()
                get2061precipMAYB()
                get2061maxaugtempB()
                get2061BIO6B()
                get2061BIO19B()
                get2061BIO16B()

            mintemp = matchminfebtemp2061B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2061B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2061B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62061B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192061B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162061B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        if stringer=="5":
            if ender == 1:
                get2081minfebtempB()
                getelevation()
                get2081precipMAYB()
                get2081maxaugtempB()
                get2081BIO6B()
                get2081BIO19B()
                get2081BIO16B()

            mintemp = matchminfebtemp2081B(float(longitude), float(latitude))
            print(mintemp)
            el = matchel(float(longitude), float(latitude))
            print(el)
            precipMAY = matchprecipMAY2081B(float(longitude), float(latitude))
            print(precipMAY)
            maximumtempaug = matchmaxtempAUG2081B(float(longitude), float(latitude))
            print(maximumtempaug)
            biolog6 = matchBIO62081B(float(longitude), float(latitude))
            print(biolog6)
            biolog19 = matchBIO192081B(float(longitude), float(latitude))
            print(biolog19)
            biolog16 = matchBIO162081B(float(longitude), float(latitude))
            print(biolog16)

            finalresult = []
            finalresult.append(mintemp)
            finalresult.append(el)
            finalresult.append(precipMAY)
            finalresult.append(maximumtempaug)
            finalresult.append(biolog6)
            finalresult.append(biolog19)
            finalresult.append(biolog16)
            print(finalresult)

        if stringer=="1":
            if model == "2":
                thepred=Neural(finalresult, codeval)
                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

            elif model == "3":

                thepred=Linear(finalresult, codeval)
                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

            elif model == "4":

                thepred=Logit(finalresult, codeval)
                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

        elif stringer!="1":
            if model == "2":

                thepred=futureNeural(finalresult, codeval)
                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

            elif model == "3":
                thepred=futureLinear(finalresult, codeval)
                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')

            elif model == "4":
                thepred=futureLogit(finalresult, codeval)
                doublearray = thepred[0]
                yesfinal = str(doublearray[1])

                sheet1.write(ender, 0, longitude)
                sheet1.write(ender, 1, latitude)
                sheet1.write(ender, 2, yesfinal)

                wb.save('C:/Users/aviba/Desktop/Map/YourMap.xls')




