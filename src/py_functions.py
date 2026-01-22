# 1BASIC FUNCTION
def greet():
    print("Hello, Welcome!")

greet()

print("\n-----------------------------\n")

# --------------------------------------------------
#  FUNCTION WITH PARAMETERS
def greet_user(name):
    print("Hello", name)

greet_user("Jayadheep")

print("\n-----------------------------\n")

# --------------------------------------------------
#  FUNCTION WITH RETURN VALUE
def add(a, b):
    return a + b

result = add(10, 5)
print("Addition Result:", result)

print("\n-----------------------------\n")

# --------------------------------------------------
#  MULTIPLE RETURN VALUES
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calculate(10, 5)
print("Sum:", sum_)
print("Difference:", diff)
print("Product:", prod)

print("\n-----------------------------\n")

# --------------------------------------------------
#  DEFAULT PARAMETERS
def greet_default(name="Guest"):
    print("Hello", name)

greet_default()
greet_default("Ravi")

print("\n-----------------------------\n")

# --------------------------------------------------
#  KEYWORD ARGUMENTS
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)

student_details(age=21, name="Arjun")

print("\n-----------------------------\n")

# --------------------------------------------------
#  *args (VARIABLE LENGTH ARGUMENTS)
def total_sum(*numbers):
    return sum(numbers)

print("Total Sum:", total_sum(1, 2, 3, 4, 5))

print("\n-----------------------------\n")

# --------------------------------------------------
#  **kwargs (KEY-VALUE ARGUMENTS)
def user_details(**details):
    for key, value in details.items():
        print(key, ":", value)

user_details(name="Jay", role="Backend Dev", experience=2)

print("\n-----------------------------\n")

# --------------------------------------------------
#  NESTED FUNCTION
def outer_function():
    print("Outer function running")

    def inner_function():
        print("Inner function running")

    inner_function()

outer_function()

print("\n-----------------------------\n")

# --------------------------------------------------
 #LAMBDA FUNCTION
square = lambda x: x * x
print("Square of 5:", square(5))

print("\n-----------------------------\n")
