import random
n = int(input())
nums = [random.randint(0, 100) for x in range(n)]
print(nums)
nums.sort()
print("Min Value:", nums[0])
print("Max Value:", nums[len(nums)-1])