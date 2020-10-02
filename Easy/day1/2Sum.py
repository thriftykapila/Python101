def twoSum(nums: [], target: int):
    # r = dict()
    # for i in range(len(nums)):
    #   if target-nums[i] in r:
    #     return [r[target-nums[i]],i]
    #   else:
    #     r[nums[i]]=i
    # return r

    r = []
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in r:
            return [nums.index(temp), i]
        r.append(nums[i])


print(twoSum(nums=[0, 4, 3, 0], target=0))

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
