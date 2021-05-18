import os
import xml.dom.minidom
from xml.dom.minidom import parse

#import the files
os.chdir('E:\\study\\Semester2\\ELSE\\IBI\\Practical14')
DOM= xml.dom.minidom.parse("go_obo.xml")
collection = DOM.documentElement

#Read the file and make a DOM tree
terms= collection.getElementsByTagName('term')        

#Define a function that count the childnode number of 'a'-assosiated terms
def countnum(a):                
    count=0
    #Get the element 'term'
    for term in terms:                    
        #Get the element 'defstr'
        defstr=term.getElementsByTagName('defstr')      
        if a in defstr[0].firstChild.data:                     
            # If 'a' exists in 'defstr', then read the 'is_a' of it
            subclass=term.getElementsByTagName('is_a')           
            for is_a in subclass:
                count= count+ 1                  #Add the counts
    
    
    print('The childnode number of '+a+' is '+ str(count)+'.')
    return count

DNA=countnum('DNA')
RNA=countnum('RNA')
Protein=countnum('protein')

#Get the number of childNotes related with carbohydrate
GP=countnum('glycoprotein')                  
import matplotlib.pyplot as plt
dic={'DNA':DNA,'RNA':RNA,'Protein':Protein,'glycoprotein':GP}

#Get the sum of all cases
sum= dic['DNA']+dic['RNA']+dic['Protein']+dic['glycoprotein']      
labels='DNA','RNA','Protein','glycoprotein'

# the percentage of cases is count by "100*X/sum"
# make the plot
sizes=[100*dic['DNA']/sum,100*dic['RNA']/sum,100*dic['Protein']/sum,100*dic['glycoprotein']/sum]
explode=(0,0.1,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('The childNodes number of different molequle-assosiated terms.')
plt.show() 