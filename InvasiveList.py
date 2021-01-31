import csv
finalarr=[]
with open('InvasiveList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        arr=row
        stringer=""
        for x in range (len (arr [0])):
            if arr [0][x]=="(":
                break
            else:
                stringer+=arr [0][x]

        finalarr.append (stringer)

print (finalarr)

import xlsxwriter

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

content = finalarr

for item in content:
    worksheet.write(row, column, item)
    row += 1

workbook.close()




