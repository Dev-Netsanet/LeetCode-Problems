from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        rightSum = 0
        ans = []
        for Rsum in range(len(nums)):
            rightSum += nums[Rsum]
        for i in nums:
            rightSum -= i
            ans.append(abs(leftSum - rightSum))
            leftSum += i
        return ans
sol = Solution()
a= [10, 4, 8 ,3]
print(sol.leftRightDifference(a))