#7.1 Write a program to read through a file and print the contents of the file (line by line) all in upper case. 

import os

try:
    fread = open('/Users/pablobartolome/Documents/Python/files/mbfox.txt')
except:
    print ('File cannot be opened')
    os._exit(1) #need it to stop the app

for line in fread:
    print (line.upper())

