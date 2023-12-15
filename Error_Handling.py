from os import path

file_name = "data.txt"

if not path.exists(file_name):
    print("No such file or directory")
else:
    with open(file_name) as file:
        print(file.readlines())

x = 10
y = 1
try:
    with open(file_name) as file:
        print(file.readlines())

    z = x / y
    print(z)

except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Task completed")
