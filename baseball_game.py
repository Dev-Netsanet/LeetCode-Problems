class Solution:
    def valid(self):
        stack = []
        s = '(}'
        close = {')':'(' , '}':'{', ']':'['}
        for c in s:
            if c in close:
                if stack and stack[-1]== close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack

sol = Solution()
print(sol.valid())
        
            