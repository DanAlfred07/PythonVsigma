# Indexing and Slicing

# Indexing
import numpy as np
var = np.array([1, 2, 3, 4])

print(var[1])
print(var[-1])


var = np.array([[1,2,3,4],[1,2,3,4]])
print(var[0,1])

var = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(var[0,0,1])

# slicing

var = np.array([1,2,3,4])
print(var[1:])
print(var[1:3])