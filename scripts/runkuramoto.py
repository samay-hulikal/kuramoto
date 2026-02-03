import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from src.kuramoto import Kuramoto

# Run the model
# sim = Kuramoto(N = 10, K = 1, stdomega = 0.01, Kenv = 0.8, envomega = 2) # Synchronized, but tugged by environment; no synchrony with environment

# sim = Kuramoto(N = 10, K = 0.005, stdomega = 0.01, Kenv = 1, envomega = 2) # Not synchronized; synchronized partially by environmental tugging; not synchronized with environment

# sim = Kuramoto(N = 10, K = 0.005, stdomega = 0.01, Kenv = 2, envomega = 2) # Not synchronized; synchronized fully by environmental tugging; not synchronized with environment

sim = Kuramoto(N = 10, K = 0.005, stdomega = 0.01, Kenv = 5, envomega = 2) # Not synchronized; synchronized fully by environmental tugging; synchronized with environment

# Storing the data
time = []
order = []
theta = []
position = []

for k in range(500):
    time.append(sim.time)
    order.append(sim.orderparameter())
    theta.append(sim.theta.copy())
    position.append(sim.position().copy())
    sim.step(dt = 0.1)

time = np.array(time)
order = np.array(order)
theta = np.array(theta)
position = np.array(position)

# Plotting the phase of the oscillators
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (12, 9))

for i in range(sim.N):
    ax1.plot(time, theta[:, i] % (2 * np.pi), alpha = 0.6, linewidth = 0.6)
ax1.plot(time, sim.envomega * time % (2 * np.pi), alpha = 1, linewidth = 2)
ax1.grid(True, alpha = 0.4)
ax1.set_xlabel(r'$t$', fontsize = 10)
ax1.set_ylabel(r'Phase $\theta$', fontsize = 10)
ax1.set_title(f'Phase plot for N = {sim.N}, K = {sim.K:.2f}, var = {sim.stdomega:.2f}, K (env) = {sim.Kenv:.2f}, env. frequency = {sim.envomega}')

ax2.plot(time, order, 'r-', linewidth = 2)
ax2.grid(True, alpha = 0.4)
ax2.set_xlabel(r'$t$', fontsize = 10)
ax2.set_ylabel(r'Order parameter $|<e^{i\theta}>|$', fontsize = 10)
ax2.set_title(f'Order parameter for N = {sim.N}, K = {sim.K:.2f}, var = {sim.stdomega:.2f}, K (env) = {sim.Kenv:.2f}, env. frequency = {sim.envomega}')

plt.tight_layout()
plt.savefig(f'figures/N_{sim.N}_K_{sim.K:.2f}_var_{sim.stdomega:.2f}_Kenv_{sim.Kenv:.2f}_envfreq_{sim.envomega}.svg')
plt.show()
