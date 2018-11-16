fhand = open('/Users/pablobartolome/Documents/Python/files/mbox.txt')
count = 0

for line in fhand:
    count += 1
print ('Total lines: ', count)

print ('----------')

fhand = open('/Users/pablobartolome/Documents/Python/files/mbox.txt')
count = 0
a = fhand.read() #save all content into a string
print (a[:50])

print ('----------')

fhand = open('/Users/pablobartolome/Documents/Python/files/mbox.txt')
count = 0

for line in fhand:
    line.rsplit()
    if line.startswith('From'):
        print (line)