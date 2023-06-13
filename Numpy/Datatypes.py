# Data Types
import numpy as np
var = np.array([1,2,3,4])
print("Datatype: ",var.dtype)

var = np.array([1.0,2.0,3.4,4.6])
print("Datatype: ",var.dtype)

var = np.array(["a","b","c","d"])
print("Datatype: ",var.dtype)

var = np.array([1,2,3,4],dtype = np.int8)
print("Datatype: ",var.dtype)

var = np.array([1,2,3,4],dtype = "f")
print("Datatype: ",var.dtype)
print(var)

var = np.array([1,2,3,4])
new = np.float32(var)
print("Datatype: ",var.dtype)
print("Datatype: ",new.dtype)
print(var)
print(new)

var = np.array([1,2,3,4])
new = var.astype(float)
print(var)
print(new)
