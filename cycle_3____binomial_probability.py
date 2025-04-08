import math

def binomial_probability(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

n = 6
p = 0.025

prob_4 = binomial_probability(n, 4, p)
print("Probability of exactly 4 successes:", prob_4)

prob_at_1 = 1 - binomial_probability(n, 0, p)
print("Probability of at least 1 success:", prob_at_1)
