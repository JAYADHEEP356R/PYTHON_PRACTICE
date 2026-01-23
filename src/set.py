# Creating sets
numbers = {1, 2, 3, 4, 5}
duplicates = {1, 2, 2, 3, 3, 4}

print("Numbers Set:", numbers)
print("Duplicates removed automatically:", duplicates)

# Creating an empty set
empty_set = set()
print("Empty set:", empty_set)

# Adding elements
numbers.add(6)
print("After add:", numbers)

# Adding multiple elements
numbers.update([7, 8, 9])
print("After update:", numbers)

# Removing elements
numbers.remove(3)   # raises error if not found
print("After remove:", numbers)

numbers.discard(10) # no error if not found
print("After discard:", numbers)

# Pop (removes random element)
removed = numbers.pop()
print("Popped element:", removed)
print("After pop:", numbers)

# Set length
print("Length of set:", len(numbers))

# Looping through set
print("\nLooping through set:")
for n in numbers:
    print(n)

# Checking membership
print("Is 5 in set?", 5 in numbers)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\nUnion:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)

# Set comprehension
squares = {x * x for x in range(1, 6)}
print("\nSet comprehension:", squares)

# Frozen set (immutable set)
fs = frozenset([1, 2, 3])
print("Frozen set:", fs)