class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1,n):
            if i%15==0:
                answer.append("FizzBuzz")
            elif i%5==0:
                answer.append("Buzz")
            elif i%3==0:
                answer.append("Fizz")
            else:
                answer.append(str(i))
        return answer

solution = Solution()
sl = solution.fizzBuzz(15)
print(sl)


