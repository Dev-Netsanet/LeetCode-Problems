class Solution:
    def convertTemperature(self):
        ans = []  
        celsius = float(input("Input celsius: "))
        kelvin = float(celsius + 273.15)
        kelvins = round(kelvin, 5)
        ans.append(kelvins)
        Fahrenheit = float(celsius *1.80 + 32.00)
        Fahrenheits = round(Fahrenheit, 5)
        ans.append(Fahrenheits)
        return ans
cel = Solution()

print(f"output: {cel.convertTemperature()}")
