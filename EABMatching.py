import pandas as pd


EAB=[]
ab=[]
Good=[]
mintemparr=[]
result=[]
elevation=[]
precipitationMAY=[]
avgtempfeb=[]
windapril=[]
maxtempaug=[]
BIO6=[]
BIO19=[]
BIO16=[]

def getEAB ():
    with open ('JustLatLon(EAB).csv', 'r') as g:
        for line in g:
            line=line.strip ()
            EAB.append(line.split (","))
def getab ():
    with open ('NEWNEWAbscence.csv', 'r') as g:
        for line in g:
            line=line.strip ()
            ab.append(line.split (","))

def abmatch (lon, lat):
    for y in range (len (EAB)):
        if (abs((float(lon)) - float(EAB [y][0]))) + (abs((float(lat)) - float(EAB [y][1])))<0.5:
            Good.append(-10000)
            return
    Good.append (1)

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
    with open('C:/Users/aviba/PycharmProjects/colors/Model Files/dprecipitationMAY.txt', 'r', errors='ignore') as f:
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

def match (lon, lat):
    min=10000
    minindex=-1
    for x in range (len (mintemparr)):
        if (abs ((float (lon))-float (mintemparr [x][0])))+(abs ((float (lat))-float (mintemparr [x][1])))<min:
           min=(abs ((float (lon))-float (mintemparr [x][0])))+(abs ((float (lat))-float (mintemparr [x][1])))
           #print(min)
           minindex=x
    result.append(mintemparr [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/febarr.xlsx")
    print (result)

def matchel (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (elevation)):
        if (abs ((float (lon))-float (elevation [x][0])))+(abs ((float (lat))-float (elevation [x][1])))<min:
           min=(abs ((float (lon))-float (elevation [x][0])))+(abs ((float (lat))-float (elevation [x][1])))
           #print(min)
           minindex=x
    result.append(elevation [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/ELEVATION.xlsx")
    print (result)

def matchprecipMAY (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (precipitationMAY)):
        if (abs ((float (lon))-float (precipitationMAY [x][0])))+(abs ((float (lat))-float (precipitationMAY [x][1])))<min:
           min=(abs ((float (lon))-float (precipitationMAY [x][0])))+(abs ((float (lat))-float (precipitationMAY [x][1])))
           #print(min)
           minindex=x
    result.append(precipitationMAY [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/PRECIPITATIONMAY.xlsx")
    print (result)

def matchavgtempfeb (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (avgtempfeb)):
        if (abs ((float (lon))-float (avgtempfeb [x][0])))+(abs ((float (lat))-float (avgtempfeb [x][1])))<min:
           min=(abs ((float (lon))-float (avgtempfeb [x][0])))+(abs ((float (lat))-float (avgtempfeb [x][1])))
           #print(min)
           minindex=x
    result.append(avgtempfeb [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/AVERAGETEMPERATUREFEB.xlsx")
    print (result)

def matchwindapril (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (windapril)):
        if (abs ((float (lon))-float (windapril [x][0])))+(abs ((float (lat))-float (windapril [x][1])))<min:
           min=(abs ((float (lon))-float (windapril [x][0])))+(abs ((float (lat))-float (windapril [x][1])))
           #print(min)
           minindex=x
    result.append(windapril [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/WINDAPRIL.xlsx")
    print (result)

def matchmaxtempaug (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (maxtempaug)):
        if (abs ((float (lon))-float (maxtempaug [x][0])))+(abs ((float (lat))-float (maxtempaug [x][1])))<min:
           min=(abs ((float (lon))-float (maxtempaug [x][0])))+(abs ((float (lat))-float (maxtempaug [x][1])))
           #print(min)
           minindex=x
    result.append(maxtempaug [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/MAXTEMPAUG.xlsx")
    print (result)

def matchBIO6 (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO6)):
        if (abs ((float (lon))-float (BIO6 [x][0])))+(abs ((float (lat))-float (BIO6 [x][1])))<min:
           min=(abs ((float (lon))-float (BIO6 [x][0])))+(abs ((float (lat))-float (BIO6 [x][1])))
           #print(min)
           minindex=x
    result.append(BIO6 [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/BIO6.xlsx")
    print (result)

def matchBIO19 (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO19)):
        if (abs ((float (lon))-float (BIO19 [x][0])))+(abs ((float (lat))-float (BIO19 [x][1])))<min:
           min=(abs ((float (lon))-float (BIO19 [x][0])))+(abs ((float (lat))-float (BIO19 [x][1])))
           #print(min)
           minindex=x
    result.append(BIO19 [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/BIO19.xlsx")
    print (result)

def matchBIO16 (lon, lat):
    min=1000000
    minindex=-1
    for x in range (len (BIO16)):
        if (abs ((float (lon))-float (BIO16 [x][0])))+(abs ((float (lat))-float (BIO16 [x][1])))<min:
           min=(abs ((float (lon))-float (BIO16 [x][0])))+(abs ((float (lat))-float (BIO16 [x][1])))
           #print(min)
           minindex=x
    result.append(BIO16 [minindex][2])
    df = pd.DataFrame(result)
    df.to_excel(excel_writer="C:/Users/aviba/Desktop/BIO16.xlsx")
    print (result)

getEAB()
getBIO16 ()

for x in range (0, len (EAB)):
    matchBIO16 (EAB [x][0], EAB [x][1])
print (result)


#getab ()
#for x in range (0, len (ab)):
    #abmatch (ab [x][0], ab [x][1])
#df = pd.DataFrame(Good)
#df.to_excel(excel_writer="C:/Users/aviba/Desktop/EABOutputs/GoodAbscenceNEW.xlsx")

