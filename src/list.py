# list_in_python.py
# Demonstration of Python Lists

# Creating a list
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

print("Numbers:", numbers)
print("Names:", names)

# Accessing elements (indexing)
print("First number:", numbers[0])
print("Last name:", names[-1])

# Modifying elements
numbers[2] = 99
print("After modification:", numbers)

# Adding elements
numbers.append(6)
print("After append:", numbers)

numbers.insert(1, 10)
print("After insert:", numbers)

# Removing elements
numbers.remove(10)
print("After remove:", numbers)

last_item = numbers.pop()
print("Popped item:", last_item)
print("After pop:", numbers)

# List length
print("Length of list:", len(numbers))

# Looping through a list
print("Looping through numbers:")
for num in numbers:
    print(num)

# List comprehension
squares = [x * x for x in numbers]
print("Squares using list comprehension:", squares)

# Checking membership
print("Is 99 in numbers?", 99 in numbers)

# Sorting a list
numbers.sort()
print("Sorted list:", numbers)

# Reversing a list
numbers.reverse()
print("Reversed list:", numbers)

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
