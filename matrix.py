import numpy as np
import pandas as pd
from numpy import linalg as LA

M = np.array([
    [1, -1],
    [2, 4]
])

## find the eigenvalues for a matrix:
print(LA.eig(M))

## find the inverse of a matrix:
print(LA.inv(M))
