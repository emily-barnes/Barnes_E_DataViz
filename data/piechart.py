import matplotlib.pyplot as plt 

values = [386, 239]
colors = ['green', 'blue']
labels = ["Men", "Women"]

explode = (0, 0.1)




plt.pie(values, labels=labels, colors=colors, explode=explode)




plt.show()