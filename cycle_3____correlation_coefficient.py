import numpy as np

hand_size = [17, 15, 19, 17, 21]
height = [150, 154, 169, 172, 175]

a = np.array(hand_size)
b = np.array(height)

corr_matrix = np.corrcoef(a, b)
res = corr_matrix[0, 1]

print("Correlation Coefficient:", res)

if res > 0:
    print("Positive correlation")
elif res < 0:
    print("Negative correlation")
else:
    print("No correlation between hand size and height")
