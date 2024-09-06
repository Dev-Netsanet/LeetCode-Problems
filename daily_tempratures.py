from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        res = []
        index = 0
        for i, temp in enumerate(temperatures):
            while res and temperatures[res[-1]] < temp:
                x = res.pop()
                ans[x] = i - x
            res.append(i)
        return ans
t = [73,74,75,71,69,72,76,73]
sol = Solution()
print(sol.dailyTemperatures(t))