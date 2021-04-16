import os
import re

#open the file and make sure the result will be output in this dictionary
os.chdir('E:\\study\\Semester2\\ELSE\\IBI\\Practical8')
f = open( 'E:\\study\\Semester2\\ELSE\\IBI\\Practical8\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

#use a to store the sequence
a = ''
#use b to store the whole sentence
b =''

#use Bloose to to control the loop
Boole = False
k=0

for line in f:
        if line.startswith('>'):
                if Boole==True:
                         b=b+'>'+d+'  '+str(len(a)-k)+'\n'+a+'\n'
                         a=''
                         k=0
                         Boole==False
                if re.findall(r'unknown',line):
                        d=re.findall(r'^>.+?_',line)
                        d=d[0]
                        d=d[:-1]
                        Boole=True
        else:
                if Boole==True:
                        a=a+line.strip()+'\n'
                        #to avoid '\n' being counted into the lenth of seruence
                        k=k+1
f.close()
#write the result in a new file 
q=open('unknown_function.fa','w')
q.write(b)
q.close()



                       
                