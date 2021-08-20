#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:32:43 2021

@author: chiaweijie
"""
DatasetToProcess='dataset2.csv'#decide dataset to process
ProcessedOutput='ProcessedOutput.csv'#decide filename for processed data

import re
import csv
  
def Process_File():
    #Declare header
    header = ['first_name','last_name','price','above_100']
    #Read CSV and clean up data
    with open(DatasetToProcess) as f: 
        z,a=[],[] #list to contain cleaned dataset
        for line in f:
            x=(line.rstrip('\n').split(','))  #split csv by ','
            y=(x[0].split()) #split first name and last name by space into list y
            y.append(x[1])#append price into y
            z.append(y)# append completed list y into a empty list
    for i in range(len(z)):
       for j in range(len(z[i])): # to clean up unwanted field
            if z[i][j]=='name' or z[i][j]=='price' or re.search ("Mr.",z[i][j]) or re.search ("Mrs.$",z[i][j])  or re.search ("Dr.$",z[i][j]) or re.search ("Ms.$",z[i][j]) or re.search ("Miss$",z[i][j]) or re.search ("MD$",z[i][j]) or re.search ("DDS$",z[i][j]) or re.search ("III$",z[i][j]) or re.search ("DVM$",z[i][j]) or re.search ("Jr.$",z[i][j]) or re.search ("PhD$",z[i][j]) or re.search ("II$",z[i][j]) or re.search ("IV$",z[i][j]):
                z[i][j]='' # replace with empty string
       a.append(z[i]) #append into new list
    new_list=[[s for s in l if len(s)>0] for l in a] #remove empty string in list
    new_list2=[x for x in new_list if x]#remove empty list=>remove row from csv
    #To populate above_100 column
    for i in range(len(new_list2)):
        if int(float(new_list2[i][-1]))>100:
            new_list2[i].append(True)
        else:
            new_list2[i].append(False)
    #write into CSV
    with open(ProcessedOutput, 'w', encoding='UTF8', newline='') as f: # write list into file
        writer=csv.writer(f)
        writer.writerow(header)        
        writer.writerows(new_list2)
Process_File()


'''
For the scheduling component, 
if using mac,
add a new job to crontab by using the cmd crontab -e and add the python schedule script. etc below.
00 13 * * * cd /users/username/ && /usr/bin/python Section1_v0.3py
This will run the python file at 1am everyday.

if using window server 
1) you can setup a bat script to run this python file and set up a daily job 
in window task scheduler where it will trigger the bat at 1am everyday.

For more robust proceesing as this py file require to specify name for input and output files,
1) Do dir /b ->filename.txt in cmd to retrieve the filenames for multiple files. Push this file 
into a database and retrieve the file name one by one as a variable and push into this py.
2) After the file is processed, update the processed indicator flag column in DB and repeat 
until all files are processed. 
'''

