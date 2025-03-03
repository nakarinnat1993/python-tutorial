import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a)

result_add = a + b
print(result_add)

result_mul = a * b
print(result_mul)

mean = np.mean(a)  # AVG
std_dev = np.std(a)
print("Mean:", mean, "Std Dev:", std_dev)

