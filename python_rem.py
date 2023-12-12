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


python_dic()
