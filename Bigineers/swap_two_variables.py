a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Original values")
print(f"a = {a} and b = {b}")

a, b = b, a

print("After swap")
print(f"a = {a} and b = {b}")
