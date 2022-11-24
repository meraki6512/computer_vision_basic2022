import numpy as np
nums = np.array([[1,4,2],[7,5,3]])
print(nums)
print(nums[0,2])
print(nums[0][2])
#row
print(nums[0:1,])
print(nums[0:1,:])
#col
print(nums[:, 1:2])
#row, col
print(nums[1, 1:]) #index
print(nums[0:, 1:]) #range

#index vs range
print(nums[0:1,])
print(nums[0:1,:])
print(nums[0,:])


