import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr3)

# Reshaping
reshaped = arr1.reshape(5, 1)
print("\nReshaped 1D to 2D:\n", reshaped)

# Slicing
print("\nSlicing 1D (index 1 to 3):", arr1[1:4])
print("Slicing 2D (first row):", arr2[0])
print("Slicing 2D (element):", arr2[1][2])

# Indexing
print("\nIndexing 1D:", arr1[2])
print("Indexing 2D:", arr2[1, 1])
print("Indexing 3D:", arr3[1, 0, 1])