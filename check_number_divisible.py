num = int(input('Number: '))
Numbers = []

for i in range(1, num+1):
    if num % i == 0:
        Numbers.append(i)
        continue
print(Numbers)
