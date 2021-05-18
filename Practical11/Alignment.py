import os
import re

#open files
os.chdir('E:\\study\\Semester2\\ELSE\\IBI\\Practical11')
h = open( 'E:\\study\\Semester2\\ELSE\\IBI\\Practical11\\SOD2_human.fa')
m = open( 'E:\\study\\Semester2\\ELSE\\IBI\\Practical11\\SOD2_mouse.fa')
r = open( 'E:\\study\\Semester2\\ELSE\\IBI\\Practical11\\RandomSeq.fa')

#input sequences
for line in h:
        if line.startswith('>'):
          n1 = re.findall(r'.+',line)
          n1=n1[0]
        else:  
          seq1=re.findall(r'.+',line)
          seq1=seq1[0]
for line in m:
        if line.startswith('>'):
          n2 = re.findall(r'.+',line)
          n2=n2[0]
        else:  
          seq2=re.findall(r'.+',line)
          seq2=seq2[0]
for line in r:
        if line.startswith('>'):
          n3 = re.findall(r'.+',line)
          n3=n3[0]
        else:  
          seq3=re.findall(r'.+',line)
          seq3=seq3[0]
amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']

#input the blosum
blosum = [
[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]

#calculate alignment scores
def alig(seq1,seq2):
  edit_distance = 0
  for i in range (len(seq1)):  
    if seq1[i] != '\n':
      a = amino.index(seq1[i])
      b = amino.index(seq2[i])
      edit_distance = edit_distance + blosum[a][b]
  return edit_distance

#calculate percentage of identical amino acids
def per(seq1,seq2):
  k = 0
  for i in range (len(seq1)):
    if seq1[i] == seq2[i]:
      k = k + 1
  per = k / len(seq1) * 100

  return per

#output results
print('The alignment score between human and mouse is', alig(seq1,seq2), 'The percentage of identical amino acids is',format(per(seq1,seq2),'1f'),'%')
print('The alignment score between human and random is', alig(seq1,seq3), 'The percentage of identical amino acids is',format(per(seq1,seq3),'1f'),'%')
print('The alignment score between mouse and random is', alig(seq2,seq3), 'The percentage of identical amino acids is',format(per(seq2,seq3),'1f'),'%')

#Comparing to the random sequence, human sequence and mouse sequence have similar alignment scores.
#Their percentages of identical amino acids comparing to the random sequence are similar.
#As human and mouse are both mammal, their percentage of identical amino acids is relatively high.
#The alignment score between human and mouse is 1091.