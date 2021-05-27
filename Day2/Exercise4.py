my_list1 = [20, "apple", 6.25]
print(my_list1)

my_list2 = [1, 1, [1, 2]]
print(my_list2[2][1])

lst = ['a', 'b', 'c']
lst[1:]  # ['b', 'c']

my_week = {'sunday': 0, 'monday': 1, 'tuesday': 2,
           'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6}

D = {'k1': [1, 2, 3]}
# output of d[k1][1]
# d and k1 does not exist, but D['k1'][1] is 2

my_list3 = [1, [2, 3]]
tuple(my_list3)

my_state = set('Mississippi')

my_state.add('X')

# Output of set([1, 2, 3])
#{1, 2, 3}

# Question 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).


def multiples():
    numbers = set()
    for i in range(2002, 3201, 7):
        numbers.add(i)

    for i in range(2000, 3201, 5):
        numbers.discard(i)

    casted = [str(num) for num in numbers]
    print(str(", ".join(casted)))

# Question 2: Write a program which can compute the factorial of a given number.


def calc_factorial(val: int):
    if val == 1:
        return 1
    return val * calc_factorial(val - 1)


print(calc_factorial(int(input("Enter number for factorial:"))))

# Question 3:With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.


def create_sqr_dict(num: int):
    val = dict()
    for i in range(1, num + 1):
        val[i] = i*i
    return val


val = int(input())
print(create_sqr_dict(val))

# Question 4: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
val = input("Enter numbers separated by commas:\n")
my_list = list(val.split(","))
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)


class IOString(object):
    def __init__(self):
        self.s = ""

    def inputString(self):
        self.s = input

    def printString(self):
        print(self.s.upper())


ioString = IOString()
ioString.inputString()
ioString.printString()
