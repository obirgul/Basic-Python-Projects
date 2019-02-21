import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(array1)  # 1*4 vector
print(array1.shape)

a = array1.reshape(3, 5)
print(a)
print("Shape: ", a.shape)
print("Dimension: ", a.ndim)

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array)
print("Shape: ", array.shape)
print("Dimension: ", array.ndim)


zeros = np.zeros((3, 3))
ones = np.ones((3, 3))
empty = np.empty((3, 3))

zeros[1, 1] = 5
print(zeros)
