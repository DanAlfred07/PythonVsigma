# Converting the Lists to arrays by using Numpy

import numpy as np

x = np.array([10,20,30,40,50])
print(x)
print(type(x))
print(x.ndim)

y=[1,2,3,4]
print(y)
print(type(y))

# Creating the Numpy Array

l = []
for i in range(1,4):
    int_1 = int(input("enter : "))
    l.append(int_1)
print(np.array(l))









