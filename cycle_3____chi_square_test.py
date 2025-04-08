import numpy as np
import scipy.stats as stats

observed = np.array([[60, 54, 46, 41], [40, 44, 53, 57]])

chi2, p_value, df, expected = stats.chi2_contingency(observed)

alpha = 0.05
critical_value = stats.chi2.ppf(1 - alpha, df)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p_value}")
print(f"Degrees of freedom: {df}")
print(f"Expected frequencies:\n{expected}")
print(f"Critical value at alpha = {alpha}: {critical_value}")

if p_value < alpha:
    print("Reject the null hypothesis: There is a significant association.")
else:
    print("Fail to reject the null hypothesis: There is no significant association.")
