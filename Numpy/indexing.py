import numpy as np

num = np.array([0, 1, 20, 300, 40, 55])
a = num[5]
b = num[0:4]

num2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(num2[0, 1])
print(num2[:, 1])
print(num2[1, :])
print(num2[:, 0:1])
