import numpy as np
from src.oscillator import Oscillator

# arange, linspace, etc. 
x = np.arange(3,7.2, 2)
print("arange", x)

lns = np.linspace(0,1,10)
print("arange", lns[6:9])
print()

arr = np.array([[1, 2, 4],
                [4, 5, 6]])
result = arr**3 + 2*arr + 2
print(result)

rand = np.random.uniform(-1, 1, 10)
print(rand)

randgauss = np.random.normal(1,1,10)
print(randgauss, len(randgauss))

# Broadcasting
noscillator = 10
theta = np.random.uniform(0, 2*np.pi, noscillator)

# Kuramoto model involves calculating the difference \theta_i - \theta_j
theta_col = theta[:, np.newaxis]
theta_row = theta[np.newaxis, :]

theta_diff = theta_col - theta_row
print(theta_col.shape, theta_row.shape, theta_diff.shape)
print(theta[1] - theta[2] == theta_diff[1, 2])

arr = 7
brr = 7
if arr == 7 and brr == 7:
    print("Yello")

def fn(a):
    return (a + 1, a * 2)

print(fn(2) + fn(3), type(fn(2)), fn(3)[1])

# Create an oscillator
a = None
print(a==None)
osc = Oscillator(omega = 4)
print(osc)
osc.dtpropagate(0.5, 0)
print(osc)
