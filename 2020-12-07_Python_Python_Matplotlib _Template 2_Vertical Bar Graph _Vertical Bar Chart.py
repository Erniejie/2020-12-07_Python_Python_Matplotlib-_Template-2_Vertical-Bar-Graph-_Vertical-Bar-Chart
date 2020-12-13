#Python__Matplotlib _Template 2_VERTICAL Bar Graph _VERTICAL Bar Chart 

import matplotlib.pyplot as plt

x = ["Soil Mechanics","Structural Analysis","Hydraulics","Pystructures"]
h = [300,500,700,1000]

c = ["yellow","red","green","orange"]
#plt.bar(x,h,width=0.6,color=c)   # widht: the width of the bar
plt.bar(x,h,[0.3,0.4,0.5,0.7],color=c)   # for different width sizes
plt.xlabel("Subjects")
plt.ylabel("Number of Students")
plt.title("2020 STUDENT TAKE")
plt.show()
