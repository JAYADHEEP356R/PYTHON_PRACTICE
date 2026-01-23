# tuple_in_python.py
# Demonstration of Tuple in Python

# Creating tuples
numbers = (1, 2, 3, 4, 5)
single_element = (10,)   # comma is mandatory
mixed = (1, "Python", 3.14, True)

print("Numbers Tuple:", numbers)
print("Single Element Tuple:", single_element)
print("Mixed Tuple:", mixed)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("Slice (1 to 4):", numbers[1:4])

# Tuple is immutable (cannot modify)
# numbers[0] = 100  # ❌ This will raise TypeError

# Looping through tuple
print("\nLooping through tuple:")
for n in numbers:
    print(n)

# Tuple length
print("Length of tuple:", len(numbers))

# Tuple methods
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))

# Checking membership
print("Is 4 in tuple?", 4 in numbers)

# Tuple packing
student = "Jay", 21, "CSE"
print("\nPacked Tuple:", student)

# Tuple unpacking
name, age, dept = student
print("Unpacked Values:")
print("Name:", name)
print("Age:", age)
print("Department:", dept)

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple:", nested)

# Converting tuple to list
num_list = list(numbers)
num_list.append(6)
numbers = tuple(num_list)
print("Tuple after conversion:", numbers)
