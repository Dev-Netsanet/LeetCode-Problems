nums = [1,1,1,1]
good_pair = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if i < j:
            if nums[i] == nums[j]:
                good_pair += 1

print(good_pair)