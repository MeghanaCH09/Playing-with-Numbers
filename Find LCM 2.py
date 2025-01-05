
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

for i in range(max(num1, num2), (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i

print(f"The LCM of {num1} and {num2} is {lcm}")