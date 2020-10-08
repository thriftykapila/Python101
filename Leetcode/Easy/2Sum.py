# Solution 1 - Working - fast rank - #1

# def twoSum(nums: [], target: int):
# r = dict()
# for i in range(len(nums)):
#   if target-nums[i] in r:
#     return [r[target-nums[i]],i]
#   else:
#     r[nums[i]]=i
# return r
# print(twoSum(nums=[0, 4, 3, 0], target=0))

# Solution 2 - Working - fast rank - #2
def twoSum(nums: [], target: int):
    r = []
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in r:
            return [nums.index(temp), i]
        r.append(nums[i])


print(twoSum(nums=[0, 4, 3, 0], target=0))

# Solution 3 - Not Working

# def twoSum(nums: [], target: int):
# value=0
# index=0
# for i in range(len(nums)):
#   if(nums[i]<=target):
#     value=target-nums[i]
#     return value
#     if value in nums[i+1:]:
#       index= nums[i+1:].index(value)
#       return index
#       if(index>=0) and (index!=i):
#         return [i,index]

# print(twoSum(nums=[0, 4, 3, 0], target=0))
