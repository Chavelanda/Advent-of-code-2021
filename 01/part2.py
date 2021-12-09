import pandas as pd
import numpy as np

if __name__ == "__main__":
    depths = pd.read_csv('input.txt', sep="\n", header=None).to_numpy()
    depths = np.reshape(depths, depths.shape[0])
    counter = 0
    for i in range(1, len(depths) - 2):
        counter += 1 if depths[i+2] > depths[i-1] else 0

    print(counter)
