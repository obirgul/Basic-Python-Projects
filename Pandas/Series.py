import pandas as pd
import numpy as np

data = np.array(["ali", "veli", "ayse"])
s = pd.Series(data, index=[1, 2, 3])
print(s)

data2 = {"math": 100, "lang": 50, "sport": 90}
s2 = pd.Series(data2, index=["lang", "math", "sport"])
print(s2)

data3 = 5
s3 = pd.Series(data3)
print(s3)
