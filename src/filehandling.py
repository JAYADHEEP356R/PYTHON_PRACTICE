import os

with open("data.txt","w") as file:

    file.write("Hello Python \n")
    file.write("Hello Diggibyte")

print("statement wrote into python")


with open("data.txt", "r") as file:
    content = file.read()

print("\n2. Reading full file:")
print(content)


print("3. Reading line by line:")
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())



with open("data.txt", "a") as file:
    file.write("Appending a new line\n")

print("\n4. Data appended")
