import scipy.stats as stats
import numpy as np

sample_mean = 25
pop_mean = 20
sample_sd = 4
sample_size = 30
alpha = 0.05

tstatistic = (sample_mean - pop_mean) / (sample_sd / np.sqrt(sample_size))
dof = sample_size - 1
critical_value = stats.t.ppf(1 - alpha / 2, df=dof)

print("t-statistic:", tstatistic)
print("Critical value:", critical_value)

if abs(tstatistic) > critical_value:
    print("Reject the null hypothesis: The sample mean is significantly different from the population mean.")
else:
    print("Fail to reject the null hypothesis: The sample mean is not significantly different from the population mean.")
