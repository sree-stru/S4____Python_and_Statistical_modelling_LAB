import matplotlib.pyplot as plt
import numpy as np

x=np.array(["Africa", "Asia","Europe","North America","Oceania","South America","Soviet Union"])
y=np.array([11.7,10.4,7.9,9.4,3.3,6.9,7.9])
colors=['blue','green','red','orange','purple','pink','cyan']

plt.bar(x,y,color=colors)
plt.title("BARGRAPH")
plt.xlabel("continents")
plt.ylabel("area(million square miles)")
plt.xticks(rotation=45)
plt.ylim(0,12)
plt.legend()
plt.show()


