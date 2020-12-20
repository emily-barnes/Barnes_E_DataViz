import matplotlib.pyplot as plt 

years = [1924, 1952, 1964, 1988, 1998, 2006, 2010, 2014]


medals =[0, 0, 0, 0, 0, 58, 91, 90]

plt.plot(years, medals, linewidth=3.0)

plt.ylabel("Total Medals Awarded")

plt.xlabel("Years")

plt.title("Total Medals Won by Women Over the Years" , pad="20")

plt.show()


