import pandas as pd
import numpy as np

if __name__ == "__main__":
    commands = pd.read_csv('input.txt', sep=" ", header=None).to_numpy()
    depth, forward, aim = 0, 0, 0

    for i in range(commands.shape[0]):
        if commands[i, 0] == 'down':
            aim += commands[i, 1]
        elif commands[i, 0] == 'up':
            aim -= commands[i, 1]
        else:
            forward += commands[i, 1]
            depth += commands[i, 1]*aim

    print(forward*depth)
