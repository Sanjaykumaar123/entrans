import numpy as np
x = np.array([1,2,3,4])
y = np.array([2,4,6,8])
w = 0.0
b = 0.0
lr = 0.01
for _ in range(2000):
    y_pred = w*x + b
    dw = np.mean(2*x*(y_pred-y))
    db = np.mean(2*(y_pred-y))
    w = w - lr*dw
    b = b - lr*db
print(w,b)
