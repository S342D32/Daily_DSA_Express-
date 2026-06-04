# O(N^2)
# def two_sum(nums,target):
#   for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#       if nums[i] + nums[j] == target:
#         return i,j

# O(N^2)
# for pairs
def two_sum(nums,target):
  pairs=[]
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i] + nums[j] == target:
        pairs.append((i,j))
  return pairs


# O(N)

# def two_sum(nums,target):
#   seen={}
#   for i in range(len(nums)):
#     num = nums[i]
#     need = target-num 

#     if need in seen:
#       return seen[need],i
#     seen[num]=i

nums =[1,2,3,4,5,6]
target = 6
print(two_sum(nums,target))