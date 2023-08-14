#!/usr/bin/python

import numpy as np

array = np.array([0, 1, 2, 3])

print(array)
print(array/2)
print(array**2)
print(np.roll(array, 3))

for i in np.nditer(array):
    print(i)

matrix = np.ndarray(shape=(3,3))
for line in matrix:
    for cell in line:
        print(cell)