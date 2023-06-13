# How to create Numpy Array using Numpy Function / Special Numpy Array

# Zeros
import numpy as np
zero = np.zeros(4)
zero1 = np.zeros((2,4))

print(zero)
print()
print(zero1)

# Ones

one = np.ones(4)
one1 = np.ones((2,4))

print(one)
print()
print(one1)

# Empty

empty = np.empty(4)

print(empty)

# Range

range = np.arange(4)

print(range)

# Diagonal

dia = np.eye(4,5)
print(dia)

# LineSpace

lin = np.linspace(0,20,num=5)

print(lin)
