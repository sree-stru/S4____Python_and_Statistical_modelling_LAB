import scipy.stats as stats

n = 6
mean = 3.4

p = stats.poisson.pmf(n, mean)
print("The Poisson distribution:", p)
