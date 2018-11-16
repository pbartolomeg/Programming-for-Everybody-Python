#7.2 Write a program to prompt for a file name, and then read through the file and look for lines of the form: 
# X-DSPAM-Confidence: 0.8475

import os

path = '/Users/pablobartolome/Documents/Python/files/'
#file  = raw_input ('Please provide a file: ')
try:
    file = 'mbox.txt'
    fread = open(path + file)
except:
    print('Cannot open the file') 
    os._exit(1)

""" 
for line in fread:
    line.rsplit()
    if not line.find('X-DSPAM-Confidence: 0.8475') == -1:
        print (line)
 """
lenght = len('X-DSPAM-Confidence:')
numSpam = float(0) #convert to float
count = 0
for line in fread:
    line.rsplit()
    if not line.find('X-DSPAM-Confidence:') == -1:  # When found > not == -1
        startD = lenght + 1 # Start position
        numSpam += float (line[startD:startD + 6])
        count += 1
print (numSpam / count)  #average of SpamNumber
    

