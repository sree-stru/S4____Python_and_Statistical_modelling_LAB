import numpy as np

population = [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3514097, 897934]
murder_rate = [5.7, 5.6, 4.7, 5.6, 4.4, 2.8, 2.4, 5.8]

population = np.array(population)
murder_rate = np.array(murder_rate)

murder_pop = (population*murder_rate)/ 100000

mean     = np.mean(murder_pop)
median   = np.median(murder_pop)
varience = np.var(murder_pop)

print("Mean of population     = ", mean)
print("Median of population   = ",median)
print("Varience of population = ",varience)




 
