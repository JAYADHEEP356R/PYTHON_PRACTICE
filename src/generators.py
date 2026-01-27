#Generators are like a pausing power of the control flow ....
def numbers():

    print("one")
    yield 1

    print("two")
    yield 2

    print("three")
    yield 3


generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))


print("================================================")
#useful in data engineering to lazy fetch one line of the file at once ....

def values():

    for i in range(1,6):

        yield i


generator = values()

print(next(generator))
print(next(generator))
print(next(generator))



