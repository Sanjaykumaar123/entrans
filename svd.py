import numpy as np
A = np.array([[3, 1, 1],[-1, 3, 1]])
U, S, Vt = np.linalg.svd(A)
print(U)
print(S)
print(Vt)
