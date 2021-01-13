import csv
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


def RandomForests (array):
    import pandas as pd
    import numpy as np
    dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
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



def futureRandomForests (array):
    import pandas as pd
    import numpy as np

    dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/future2var.csv")
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

    return

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

    return


stringer=input ("Type 1 for current, type 2 for 2021-2040, type 3 for 2041-2060, type 4 for 2061-2080, type 5 for 2081-2100:, type 6 for REPORT YOUR INVASIVE: ")
if stringer=="6":
    presab=input ("Press 1 if you are reporting a prescence point, 0 if abscence: ")

invasive=input ("Press 1 for HWA, 2 for EAB: ")
longitude=input ("Enter Longitude: ")
latitude=input ("Enter Latitude: ")

if stringer=="1":
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

    if invasive=="1":
        RandomForests(finalresult)
    elif invasive=="2":
        RandomForestsEAB(finalresult)

    num+=1

if stringer== "2":
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

    if invasive=="1":
        futureRandomForests(finalresult)
    elif invasive=="2":
        futureRandomForestsEAB(finalresult)

    futurenum+=1

if stringer== "3":
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

    if invasive == "1":
        futureRandomForests(finalresult)
    elif invasive == "2":
        futureRandomForestsEAB(finalresult)
    futurenum+=1

if stringer== "4":
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

    if invasive == "1":
        futureRandomForests(finalresult)
    elif invasive == "2":
        futureRandomForestsEAB(finalresult)
    futurenum+=1

if stringer== "5":
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

    if invasive == "1":
        futureRandomForests(finalresult)
    elif invasive == "2":
        futureRandomForestsEAB(finalresult)
    futurenum+=1

if stringer== "6":
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

    futurefinalresult=[]
    futurefinalresult.append (mintemp)
    futurefinalresult.append(el)
    futurefinalresult.append(precipMAY)
    futurefinalresult.append(maximumtempaug)
    futurefinalresult.append(biolog6)
    futurefinalresult.append(biolog19)
    futurefinalresult.append(biolog16)

    if presab==1:
        finalresult.append (1)
        print(finalresult)
    else:
        finalresult.append(0)
        print(finalresult)

    if invasive=="1":

        fields = finalresult
        with open(r'2var.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        morefields=futurefinalresult
        with open(r'future2var.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(morefields)

        lonlatarr=[]
        lonlatarr.append (longitude)
        lonlatarr.append (latitude)
        with open(r'Justlatlon.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(lonlatarr)

    if invasive=="2":

        fields = finalresult
        with open(r'PrescenceANDAbscence.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        morefields = futurefinalresult
        with open(r'PrescenceANDAbscenceFuture.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(morefields)

        lonlatarr = []
        lonlatarr.append(longitude)
        lonlatarr.append(latitude)
        with open(r'Justlatlon (EAB).csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(lonlatarr)







