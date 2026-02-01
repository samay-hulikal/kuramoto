import numpy as np

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
