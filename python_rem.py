def python_variables():
    # Complex Numbers
    complex_number = 2 + 3j
    print(type(complex_number))
    print(complex_number)

    # Escape Characters
    print("Hellow")
    print("World")
    print("=============================")
    print("Hellow \nWorld")  # next line

    print("Name\t: Sudhara")  # tab space
    print("Age\t: 28")

    print('Hi, "Good Morning"')  # escape any character
    print("In python, \\n gives us a new line")


# python_variables()


# String concatenation
def string_con():
    a = "Hello"
    b = "World"

    print(a + b)
    # print(a - b)
    # print(a / b)
    # print(a * b)
    # print(a % b)
    # print(a // b)
    # print(a**b)


# string_con()


def bool_operators():
    a = b = 20
    print(a, b)

    c = False
    d = False
    e = c == d
    f = not c

    g = c ^ d

    print(e)
    print(f)
    print(g)

    h, j = 2, 6
    print(h, j)


# bool_operators()


def name_input():
    name = input("Enter name: ")
    print("Hello,", name)


# name_input()


# Python lists
def python_lists():
    x = [21, 34, 454, 675]
    y = [1, 2]
    z = x + y
    print(x)
    print(x[0])
    x[0] = 232
    print(x)
    x.append(100)
    print(x)
    x.insert(1, 340)
    print(x)
    x.remove(100)
    x.pop(2)
    print(x)
    print(z)
    print(3 in z)
    print(2 in z)
    z.clear()
    print(z)


# python_lists()


def python_dic():
    post_codes = {"Colombo 01": 1000, "Colombo 02": 2000}
    print(post_codes)
    post_codes["Colombo 03"] = 3000
    print(post_codes)
    print(post_codes.keys())
    print(post_codes.values())
    y = post_codes.get(2, 0)
    z = post_codes.get("Colombo 03", 0)
    print(y, z)
    del post_codes["Colombo 01"]
    print(post_codes)
    post_codes.clear()
    print(post_codes)

    # Dictionary pass by reference example
    name_dic = {"sudhara": ["s", "a"], "dhananjaya": ["d", "a"]}

    fname = name_dic["sudhara"]
    fname.append("abeythunga")
    print(fname)
    print(name_dic)

    name_dic["abeythunga"] = 1
    print(name_dic)
    abe_value = name_dic["abeythunga"]
    abe_value = 2

    print(abe_value)
    print(name_dic)


# python_dic()


def python_set():
    x = {"Hello", "World", "Mariline", "Hello", "x"}
    print(x)

    x.add("Aish")
    print(x)

    x.add("hello")
    print(x)

    x.remove("Aish")
    print(x)

    # y = x['Hello'] # Didnt working
    # z = x[0] # Didnt working

    x2 = {"x", "y"}
    x3 = x.union(x2)
    print(x3)
    x4 = x | x2
    print(x4)

    print(x)
    x5 = x - x2
    print(x5)

    f = {"11": "22"}
    print("22" in f)


# python_set()


def python_tup():
    sudhara = ("sd", 28, "Sri Lanka", "Sri Lanka")
    print(sudhara)
    print(sudhara[0])
    print(sudhara.count("Sri Lanka"))
    tup = (12, "sd", 28)
    index, name, age = tup
    print(tup, index, name, age)


# python_tup()


def slicing():
    list1 = ["a", "c", "d", "t", "u"]
    print(list1[:2])
    print(list1[2:23])
    print(list1[-1])
    print(list1[-2:])
    print(len(list1))
    name = "Sudhara Dhananjaya"
    print(name[0:6])
    print(name[0])


# slicing()


# Conditioning
def conditioning():
    result = None
    mark = 809
    age = 34
    height = 168

    if mark >= 75:
        result = "Pass"

    print(result)

    if mark <= 50:
        print("F")
    elif mark > 50 and mark < 100:
        print("A")
    else:
        print("Invalid")

    if age <= 17 or age > 60:
        print("Go Away")
        exit()

    if age == 34:
        print("Pass")
    else:
        print("Dont know")

    if height > 150:
        job = "Security"
    else:
        job = "Labor"

    print(job)

    job2 = "Security2" if height > 150 else "Labor2"  # ternary operator
    print(job2)


# conditioning()


# Looping
def looping():
    list1 = [1, 45, 53, 24, 54, 4]
    for item in list1:
        print(item)

    for item in range(len(list1)):
        print(str(item) + ". " + str(list1[item]))

    for item in enumerate(list1):
        print(type(item), item)

    for item in enumerate(list1):
        print(item[0], item[1])

    for x, y in enumerate(list1):
        print(x, y)

    r = range(0, 5)
    print(type(r))
    for i in r:
        print(i)


# looping()
def python_while():
    numbers = [10, 11, 12, 13]
    count = 0
    sum = 0
    while count < 5:
        print(count)
        count += 1

    ite = 0
    while ite > len(numbers):
        sum += numbers[ite]
        ite += 1

    print(sum)


# python_while()


def total():
    numbers = [10, 11, 12, 13]
    total = 0

    for i in numbers:
        total += i
    print("Total: ", str(total))

    count = 0
    total = 0
    while count < len(numbers):
        total += numbers[count]
        count += 1
    print("Total in while loop: ", str(total))

    print(sum(numbers))


# total()


def max_number():
    numbers = [-10, -11, -12, -13, -56, -1, -13, -2]
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    print(max_num)


# max_number()


def dic_ite():
    dic = {1: "a", 2: "b", 3: "c"}
    for i in dic:
        print(type(i))

    for i in dic.items():
        num, letter = i
        print(num, letter)


# dic_ite()


def test(name, age="23"):
    print(age, name)


# test("sd")


# packed args
def packed_args(*names):
    print(type(names))
    print(names)


# packed_args("a", "b", "c")


# keywords args
def keyword_args(**params):
    print(type(params))
    print(params)


# keyword_args(a=34, c=43)


def both_args(*vals, **params):
    print(type(vals))
    print(vals)
    print(type(params))
    print(params)


# both_args(34, 54, "dsd", name="ds", age=54)


def convert_dic(name, age):
    print(name, age)


dic = {"name": "sd", "age": 23}

# convert_dic(**dic)


def list_comprehension():
    def is_odd(a):
        return a % 2 == 0

    def is_odd_string(a):
        return {a: "Even"} if a % 2 == 0 else {a: "Odd"}

    def is_odd_string_dic(a):
        return "Even" if a % 2 == 0 else "Odd"

    a = [2, 32, 4, 32, 3, 43, 6, 43, 543]
    b = [i for i in a]
    c = [is_odd(i) for i in a]
    d = [is_odd_string(i) for i in a]
    e = [is_odd_string(values) for i, values in enumerate(a) if i % 2 == 0]
    f = [
        {values: is_odd_string_dic(values)}
        for i, values in enumerate(a)
        if i % 2 == 0  # list comprehension
    ]
    g = {
        values: is_odd_string_dic(values) for i, values in enumerate(a) if i % 2 == 0
    }  # dictionary comprehension

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)


# list_comprehension()


def python_generators():
    def odd_gen(number):
        for i in range(number):
            if i % 2 == 1:
                print("Odd", i)
                yield i

    print("start")
    x = odd_gen(1000)
    for i in x:
        print("Loop", i)

    for (
        i
    ) in (
        x
    ):  # After consume a generator it cant be used again. Generator should reset before that.
        # We can call the function again and get another generator.
        print("Loop", i)

    print("finish")
    print(x)


# python_generators()


def str_format():
    name = "Sudhara"
    age = 28
    message = "Hello, {0}. You are {1} years old. ({0})".format(name, age)
    print(message)
    message = "Hello, {}. You are {:05d} years old. ()".format(name, age)
    print(message)
    message = f"Hello, {name}. You are {age:05d} years old. ()"
    print(message)


# str_format()


def comments(x: int = None, y: int = None) -> int:  # type hinting
    # program is not crashing when wrong data type passed or returned
    """
    This is do something
    @param x: first number
    @param y: second number
    @returns: multiplication of x and y
    """
    print(x * y)

    # TODO:
    # BUG:
    # FIXME:


# comments(5, 3)


def read_file():
    file = open("data.txt")
    # print(type(file))
    contents = file.read(1)
    print(contents)
    contents = file.readline()
    print(contents)

    while True:
        contents = file.readline()
        if not contents:
            break
        print(contents)

    file.close()


# read_file()


def read_file():
    with open(
        "data.txt", "w"
    ) as file:  # with open a context. after use with dont need to close file.close.
        # because with doing it automatically.
        for i in range(100):
            file.write(str(i) + "\n")

    numbers = ["1", "2", "3", "4"]
    msg = ", ".join(numbers)
    print(msg)


# read_file()


def marks_handler():
    science = {}
    math = {}
    english = {}
    unknown = {}
    name_set = set()

    with open("marks.txt") as file:
        field_names = file.readline()

        for line in file:
            line_tuple = tuple(line.split(","))
            name_set.add(line_tuple[0])

            if "Science" in line_tuple:
                science[line_tuple[0]] = int(line_tuple[2][:-1])
            elif "Math" in line_tuple:
                math[line_tuple[0]] = int(line_tuple[2][:-1])
            elif "English" in line_tuple:
                english[line_tuple[0]] = int(line_tuple[2][:-1])
            else:
                unknown[line_tuple[0]] = int(line_tuple[2][:-1])

        marks = [value for key, value in science.items()]
        print(f"Max Science Score {max(marks)}")
        marks = [value for key, value in math.items()]
        print(f"Max Math Score {max(marks)}")
        marks = [value for key, value in english.items()]
        print(f"Max English Score {max(marks)}")


# marks_handler()

import requests


def python_pip():
    response = requests.get(
        "https://www.googleapis.com/books/v1/volumes?q=harry_potter"
    )
    print(response)
    content = response.json()
    # print(content)
    print(len(content))
    print(type(content))
    first_key = next(iter(content))
    print(content[first_key])


# python_pip()


class Dog:
    name = ""
    breed = ""

    def bark(self, message):
        print("woof woof", message)


pomanarian = Dog()
print(type(pomanarian))
print(pomanarian)

pomanarian.name = "Scooby"
pomanarian.breed = "Unknown"

print(pomanarian.name, pomanarian.breed)

jerman_shepard = Dog()
print(jerman_shepard.name, jerman_shepard.breed)

pomanarian.bark("Hello")
Dog.bark(pomanarian, "Hi")
