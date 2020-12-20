import matplotlib.pyplot as plt

years = [1924, 1936, 1952, 1964, 1976, 1988, 1998, 2002, 2010, 2014]


medals =[9, 13, 17, 7, 3, 6, 49, 76, 93, 90]

plt.plot(years, medals, linewidth=3.0)

plt.ylabel("Total Medals Awarded")

plt.xlabel("Years")

plt.title("Total Medals Won by Canada Over the Years" , pad="20")

plt.show()

