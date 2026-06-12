# write a program to swap the values of two variables

# Method 1
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Original values")
print(f"a = {a} and b = {b}")

a, b = b, a

print("After swap")
print(f"a = {a} and b = {b}")

# Method 2
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Original values")
print(f"a = {a} and b = {b}")

temp = a
a = b
b = temp

print("After swap")
print(f"a = {a} and b = {b}")
