import matplotlib.pyplot as plt 
#Pie chart
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
#emphasize the largest number
explode = (0.1, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()
