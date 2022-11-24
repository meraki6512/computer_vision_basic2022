import numpy as np
nums = np.array([[1,4,2],[7,5,3]])

#1 -> 5
print(nums[1][1])

#2 -> [7 5]
print(nums[1, :2])

#3 -> [[2] \n[3]]
print(nums[:, 2:])

#4 -> [[1 4] \n[7 5]]
print(nums[:, :2])