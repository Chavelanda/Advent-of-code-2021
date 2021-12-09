import pandas as pd
import numpy as np

if __name__ == "__main__":
    commands = pd.read_csv('input.txt', sep=" ", header=None).to_numpy()
    f_idx = np.where(commands[:, 0] == 'forward')
    forwards = commands[f_idx, 1]
    d_idx = np.where(commands[:, 0] == 'down')
    downs = commands[d_idx, 1]
    u_idx = np.where(commands[:, 0] == 'up')
    ups = commands[u_idx, 1]

    print(np.sum(forwards)*(np.sum(downs) - np.sum(ups)))
