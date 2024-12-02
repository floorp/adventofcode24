import pandas as pd
import numpy as np
import inputfile as input
total = 0
multiplier = 0
sums = 0
sorrted = np.sort(input.inputfile,axis=0)
print(sorrted)
for val1 in sorrted:
    for col2 in sorrted:
        if col2[1] == val1[0]:
            multiplier= multiplier+1
    sums = val1[0] * multiplier
    multiplier = 0
    total = total+sums
    sums = 0
print(total)