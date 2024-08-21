nums = [1, 1, 1, 1]
ans = []
l = 0
index = 0
for i in range(len(nums)):
    x = nums[index] + l
    ans.append(x)
    l += nums[index]
    index += 1
print(ans)