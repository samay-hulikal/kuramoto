from src.kuramoto import Kuramoto

sim1 = Kuramoto(N = 10, K = -0.1, stdomega = 0.1, envomega = 0)
print(sim1)

for k in range(1000):
    sim1.step(dt = 0.05)
    print(sim1)
