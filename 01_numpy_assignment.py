import numpy as np

arr1 = np.arange(1,21)

print("Sum:", arr1.sum())
print("Mean:", arr1.mean())
print("Median:", np.median(arr1))
print("Std Dev:", arr1.std())
print("Indices > 10:", np.where(arr1 > 10))

arr2 = np.arange(1,17).reshape(4,4)

print("Array:\n", arr2)
print("Transpose:\n", arr2.T)
print("Row sums:", arr2.sum(axis=1))
print("Column sums:", arr2.sum(axis=0))

a = np.random.randint(1,100, size=(3,3))
b = np.random.randint(1,100, size=(3,3))

print("Array 3:\n", a)
print("Array 4:\n", b)

print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Dot Product:\n", np.dot(a, b))

arr3 = np.arange(1,13)
arr4 = arr3.reshape(3,4)

print("reshaped array:\n", arr4)