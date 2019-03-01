import numpy as np

a = np.array([10, 20, 30, 40,   50])
b = np.arange(5)
c = a - b
d = b**3
e = 10 * np.sin(a)
h = np.random.random((2, 4))
i = np.sum(a)
j = np.max(b)
k = np.min(a)
m = np.sqrt(b)

cos = np.cos(a*np.pi/180)
inverse = np.arccos(cos)

print(a@b)
print(a*b)  # elementwise product
print(e < 7)
