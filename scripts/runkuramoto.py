import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from src.kuramoto import Kuramoto

# Run the model
sim = Kuramoto(N = 10, K = 1, stdomega = 0.01, Kenv = 0.8, envomega = 2)

# Storing the data
time = []
order = []
theta = []
position = []

for k in range(10000):
    time.append(sim.time)
    order.append(sim.orderparameter())
    theta.append(sim.theta.copy())
    position.append(sim.position().copy())
    sim.step(dt = 0.05)

time = np.array(time)
order = np.array(order)
theta = np.array(theta)
position = np.array(position)

# print(theta.shape)
# print(position.shape)

# Plotting the data
fig, ax = plt.subplots(figsize = (10, 6))

ax.plot(time, order, 'r-', linewidth = 2)

plt.tight_layout()
plt.show()
