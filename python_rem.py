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


total()
