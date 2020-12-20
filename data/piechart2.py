import matplotlib.pyplot as plt 

values = [351, 159, 40]
colors = ['green', 'blue', 'gold']
labels = ["Hockey", "Skating", "Skiing"]

explode = (0, 0.1, 0.2)




plt.pie(values, labels=labels, colors=colors, explode=explode)




plt.show()