# Shape and Reshape of the Array
import numpy as np
var = np.array([[1,2,3,4],[1,2,3,4]])

print(var)
print()
print(var.shape)

var = np.array([1,2,3,4],ndmin=4)

print(var)
print(var.ndim)
print()
print(var.shape)

var = np.array([1,2,3,4,5,6])
print(var)

print()

x = var.reshape(3,2)
print(x)
