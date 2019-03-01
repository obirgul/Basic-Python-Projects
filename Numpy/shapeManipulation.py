import numpy as np

a = np.floor(10*np.random.random((3, 6)))

print(a.shape)  # a matrisinin satır sütun sayısını gösterir
print(np.ravel(a))  # a matrisini tek satır haline getirir
print(a.reshape(2, 9))
print(a.T)  # transpose
print(a.reshape(2, -1))  # matrix i ikiye böler

#%%
# stacking

b = np.floor(10 * np.random.random((3, 6)))

c = np.hstack((a, b))
d = np.vstack((a, b))

print(b)
print(c)
print(d)

#%%