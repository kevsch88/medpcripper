import csv
import os
import shutil


i = 0

# This function below does the actual raw ripping of the data from the med-pc file based on the arg1 component which is the filename of the medpcfile
def rip(arg1):
    filen = open(arg1, 'rb')
    data = csv.reader(filen, delimiter=' ')
    table = [row for row in data]
    i=0
    ttable = table ## make ttable the a different table to iterate over so that while it's being modified it doesn't fuck up the iteration.
    while i <= (len(ttable)-1):
        table[i] = filter(None, ttable[i])   ##### MEDPC outputs their files to a fked up format that isn't quite tab delim or space delim. This cleans up all the empty cells produced by reading it from the csv module.
        i += 1
    return ttable


#this function below will search the current and sub-directories for any .Subject X files that you specify in the list below.
filelist = []

######### Modify below #############
subjects = ['Subject 92','Subject 101','Subject 106','Subject 114','Subject 117','Subject 130','Subject 132','Subject 133','Subject 141','Subject 144']

######### Modify above #############

for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        for subnum in subjects:
            if name.split('.', 1)[-1] == subnum:
                i += 1
                print(i)
                filelist.append(name)



######### This is the fun part. Data from each file is put into a list of lists called 'table'. Table will look something like a excel sheet in which

######### each component of the medpc ripped sheet can be accessed with table[row][column] command. It may help to run the rip function independently in IDLE by 

######### defining the function (copy and paste it into idle. Then run rip('your-medpcfile') with the ' on each side.



######### What the script below does is run the rip against every file with your subject criteria in the current directory (run the fileripper.py in your

######### data directory)

######### 
table = []
for filename in filelist:
    table = rip(filename)
    listt = list = [str(table[0][6]),str(table[3][2]),str(table[7][1]),str(table[103][0][1:]),str(table[95][1]),str(table[81][1]),str(table[81][2]),str(table[81][3]),str(table[81][4]),str(table[81][5]),str(table[82][1]),str(table[82][2]),str(table[82][3]),str(table[82][4]),str(table[82][5]),str(table[83][1]),str(table[83][2]),str(table[83][3]),str(table[83][4]),str(table[83][5]),str(table[84][1]),str(table[84][2]),str(table[84][3]),str(table[84][4]),str(table[84][5]),str(table[85][1]),str(table[85][2]),str(table[85][3]),str(table[85][4]),str(table[85][5]),str(table[86][1]),str(table[86][2]),str(table[86][3]),str(table[86][4]),str(table[86][5]),str(table[87][1]),str(table[87][2]),str(table[87][3]),str(table[87][4]),str(table[87][5]),str(table[88][1]),str(table[88][2]),str(table[88][3]),str(table[88][4]),str(table[88][5]),str(table[89][1]),str(table[89][2]),str(table[89][3]),str(table[89][4]),str(table[89][5]),str(table[90][1]),str(table[90][2]),str(table[90][3]),str(table[90][4]),str(table[90][5])]
    b = open('icss.csv', 'a')
    a = csv.writer(b)
    a.writerows([listt])
    b.close()


#####Copy files to old data directory in the folder below current directory/DataOld
destination = "../DataOld"
for files in filelist:
    shutil.move(files, destination)
