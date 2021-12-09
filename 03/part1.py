
import pandas as pd
import numpy as np


data = pd.read_csv('input.txt', sep=" ", header=None, dtype=str)
data[0] = data[0].apply(lambda x: np.array(list(x)))
data = data[0].apply(pd.Series)
data = data.to_numpy()


gamma = ""
epsilon = ""
for col in range(data.shape[1]):
    val = np.argmax(np.bincount(data[:, col].astype(int)))
    gamma += str(val)
    epsilon += str(1 - val)

print(int(gamma, 2)*int(epsilon, 2))



