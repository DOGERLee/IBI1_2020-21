import os
import re

os.chdir('E:\\study\\Semester2\\ELSE\\IBI\\Practical10')
f=open("E:\\study\\Semester2\\ELSE\\IBI\\Practical10\\test.txt") 
line = f.read()
line = line.upper()
print(line)

transline=line[::-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g')
transline = transline.upper()
print(transline)
f.close()

fw=open( 'E:\\study\\Semester2\\ELSE\\IBI\\Practical10\\out.txt','w')
fw.write(transline)
fw.close
