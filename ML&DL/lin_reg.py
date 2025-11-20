import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

m = 0
c = 0
lr = 0.01
iterations = 20
loss_history = []

for i in range(iterations):
    y_pred = m * x + c
    dm = (-2/len(x)) * np.sum(x * (y - y_pred))
    dc = (-2/len(x)) * np.sum(y - y_pred)
    m -= lr * dm
    c -= lr * dc
    loss = np.mean((y - y_pred) ** 2)
    loss_history.append(loss)
    print(f"Iteration {i+1}: m = {m:.4f}, c = {c:.4f}, Loss = {loss:.4f}")

plt.figure(figsize=(7,5))
plt.plot(loss_history, marker='o')
plt.title("Loss vs Iterations")
plt.xlabel("Iteration")
plt.ylabel("MSE Loss")
plt.grid(True)
plt.show()


