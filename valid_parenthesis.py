class Solution:
    def backspaceCompare(self):
        s , t = "y#fo##f" , "y#f#o##f"
        a,b = [],[]
        
        for i in range(len(s)):
            if (s[i] == "#") and (a==[]):
                i += 1
            elif (s[i] == "#") and (a!=[]):
                a.pop()
            else:
                a.append(s[i])
        for j in range(len(t)):
             if (t[j]=="#") and (b== []):
               j += 1
             elif (t[j]=="#") and(b!= []):
                b.pop()
             else:
                b.append(t[j])
        return a, b

solution = Solution()

print(solution.backspaceCompare())