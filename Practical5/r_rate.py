#there are 84 students in IBI1 class
n=84
#one day a student was infected with T virus
O=1
#the R rate of T virus is 1.2
r=1.2
for i in range(1,5):
  O=O*r+O
print "number of individuals infected after 5 generations is"
print int(O)
