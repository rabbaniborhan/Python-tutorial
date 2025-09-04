##Use input() to take input from the user:
name = input("Enter your name: ")
print("Hello,", name)


##Converting Input to Numbers
age = int(input("Enter your age: "))   # Integer
height = float(input("Enter your height in meters: "))  # Float

print("Age:", age)
print("Height:", height)


##Multiple Inputs in One Line

x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)


##Example: Interactive Program

names = input("Your Name: ")
ages = int(input("Your Age: "))

print(f"Hello {name}! Next year, you'll be {age + 1} years old.")

