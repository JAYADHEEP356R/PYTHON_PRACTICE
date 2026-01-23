# Creating dictionaries
student = {
    "id": 101,
    "name": "Jay",
    "age": 21,
    "course": "Computer Science"
}

print("Student Dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))   # safer access

# Adding new key-value pairs
student["grade"] = "A"
print("After adding grade:", student)

# Updating values
student["age"] = 22
print("After updating age:", student)

# Removing elements
student.pop("course")
print("After pop:", student)

del student["id"]
print("After delete:", student)

# Looping through dictionary
print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Checking key existence
print("\nIs 'name' a key?", "name" in student)

# Dictionary length
print("Length of dictionary:", len(student))

# Dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print("Dictionary comprehension:", squares)

# Nested dictionary
employees = {
    1: {"name": "Alice", "role": "Developer"},
    2: {"name": "Bob", "role": "Tester"}
}

print("\nNested Dictionary:")
print(employees)