
# Question 1
import random


def find_nums1():
    nums = set()
    for i in range(1505, 2701, 7):
        nums.add(i)
    for i in range(1500, 2701, 5):
        nums.discard(i)
    return nums


# Question 2
def c_to_f(val: float):
    return val * 9 / 5 + 32


def f_to_c(val: float):
    return (val - 32) * 5 / 9


print(c_to_f(60))
print(f_to_c(45))


# Question 3
r = random.randint(1, 9)
while True:
    val = int(input("Enter a guess: "))
    if (val == r):
        print("Well guessed!")
        break
    else:
        print("Incorrect")

# Question 4
for i in range(0, 9):
    line = ''
    for j in range(0, 5 - (abs(4 - i))):
        line += '*'
    print(line)

# Question 5
val = input("Enter a word: ")
print(val[::-1])

# Question 6


def print_even_odd(nums: tuple):
    even = 0
    odd = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Number of even numbers: " + str(even))
    print("Number of odd numbers: " + str(odd))


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print_even_odd(numbers)

# Question 7
datalist = [1452, 11.23, 1+2j, True, 'w3resource',
            (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for data in datalist:
    print("{}: {}".format(type(data), data))

# Question 8
line = ''
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    line += str(i) + ' '
print(line)
