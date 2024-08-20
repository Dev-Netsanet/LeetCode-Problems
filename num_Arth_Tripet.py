class Solution:
    def arithmeticTriplets(self) -> int:
        nums = [0,1,4,6,7,10]
        diff = 3
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i < j < k:
                       if (nums[j] - nums[i]==diff)and (nums[k]-nums[j]==diff):
                        x = i, j, k
                        ans.append(x)
        return ans

solution = Solution()
print(solution.arithmeticTriplets())
