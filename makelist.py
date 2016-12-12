#opens a new file
file = open('file1.txt', 'w')
n = 1
#defines n as 1 and runs the process while n is less than 10
while n <= 10:
    file.write(str(n) + '. ' + input('Write something') + '\n')
    n += 1
#closes the file
file.close()
