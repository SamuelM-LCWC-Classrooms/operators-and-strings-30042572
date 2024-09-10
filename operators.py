"""
When editing your code, if you want to test a task simply put a print statement
at the bottom of the page, then inside type out its name, with the brackets, 
then run the file.

For example to run and check your solution to task 1 you would type

print(task_1())
"""

# 1.
def task_1():
    x = 10
    y = 10

    return x != y # Edit only this line

# 2.
def task_2():
    data = input("Enter something: ")
    return type(data) == str

#3.
def task_3(): # Store your completed string in a variable called message
    message = None

    # Write your code here 
    def get_an_int():
        while True:
            try:
                return int(input("Enter your age: "))
            except:
                print("Invalid age.")
    name = input("Enter your name: ")
    age = get_an_int()
    message = f"Hello, {name}, you are {age} years old!"
    # -------------------#

    return message