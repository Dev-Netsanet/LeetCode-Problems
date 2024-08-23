class Solution:
    def isValid(self, s: str) -> bool:
        ch = {'(':')','{':'}','[':']'}
        ans = []
        for i in s:
            if i in ch.keys():
                ans.append(i)
            else:
                if ans == []:
                    return False
                a = ans.pop()
                if i != ch[a]:
                    return False
        return not ans
            
sl = Solution()

print(sl.isValid("[(])"))
