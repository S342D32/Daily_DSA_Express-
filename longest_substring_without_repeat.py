# def longest_substring(s):
#   n=len(s)
#   max_len =0
#   for i in range(n):
#     seen=[]
#     for j in range(i,n):

#       if s[j] in seen:
       
#           break
#       seen.append(s[j])
#     max_len = max(max_len,len(seen))
#   return max_len




# s="acbcdefgef"
# print(longest_substring(s))

# TC:O(N^2)
# SC :O(N)


def longest_substring(s):
  n=len(s)
  max_len =0
  left =0
  seen=set()
  for right in range(n):
    while s[right] in seen:
      seen.remove(s[left])
      left+=1
    seen.add(s[right])
    max_len = max(max_len,right-left+1)
  return max_len


s="acbcdefgef"
print(longest_substring(s))

# TC:O(N)
# SC :O(N)