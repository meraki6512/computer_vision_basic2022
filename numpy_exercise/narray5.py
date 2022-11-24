import numpy as np

nums = np.array([[1,4,2], [7,5,3]])

print(nums[1,1])
print(nums[1,0:2])
print(nums[:,2:3])
print(nums[:,0:2])

nums = np.array(3)

print(nums)
print(nums.ndim)
print(nums.shape)

print(np.zeros((2,2)))
print(np.ones((1,2)))
#print(np.ones((1,1)))
print(np.full((2,2),7))

print(np.arange(0.4, 1.1, 0.1, 'int32'))