import pandas as pd
import numpy as np
import inputfile as input
total = 0

sorrted = np.sort(input.inputfile,axis=0)

for val in sorrted:
    value = abs(val[0]-val[1])
    total = total+value

print(total)