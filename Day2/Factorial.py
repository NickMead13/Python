# Question 2: Write a program which can compute the factorial of a given number.
value = int(input("Enter a number: "))
factorial = 1
for i in range(2, value + 1):
    factorial *= i
print(factorial)
