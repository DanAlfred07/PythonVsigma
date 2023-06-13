# Types of the arrays

# One Dimensional Array
import numpy as np
x = np.array([10,20,30,40])
print(x)
print(x.ndim)

# Two Dimensional Array

x = np.array([[11,22,33,44],[1,2,3,4]])
print(x)
print(x.ndim)

# Three Dimesional Array

x = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(x)
print(x.ndim)

# ndimesional Array

x = np.array([15,24,33,44], ndmin = 10 )
print(x)
print(x.ndim)
