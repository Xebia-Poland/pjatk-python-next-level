# pythontutor.com

nums = list(range(10))


for i in range(len(nums)):
    if nums[i] % 3 == 0:
        del nums[i]


for i, num in enumerate(nums):
    if nums[i] % 3 == 0:
        del nums[i]

print(nums)
