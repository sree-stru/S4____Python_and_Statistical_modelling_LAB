import matplotlib.pyplot as plt

height = [137.5]*4 + [142.5]*12 + [147.5]*16 + [152.5]*8
bins   = [135, 140, 145, 150, 155]

plt.hist(height, bins=bins, edgecolor='black')
plt.xlabel("Height (cm)")
plt.ylabel("Number of students")
plt.title("HISTOGRAM")
plt.show()
