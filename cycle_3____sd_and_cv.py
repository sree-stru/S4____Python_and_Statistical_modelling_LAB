import numpy as np

classes = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80)]
frequencies = [5, 10, 20, 40, 30, 20, 10, 5]

midpoints = [(cls[0] + cls[1]) /2   for cls in classes ]

midpoints = np.array(midpoints)
frequencies = np.array(frequencies)

mean = np.average(midpoints , weights = frequencies)
squared_deviation = (midpoints - mean)**2
weighted_squared_deviation  = frequencies * squared_deviation
variance = np.sum(weighted_squared_deviation) / np.sum(frequencies)

sd = np.sqrt(variance)
print ("SD = ",sd)
cv = (sd/mean)*100
print("CV =",cv)





