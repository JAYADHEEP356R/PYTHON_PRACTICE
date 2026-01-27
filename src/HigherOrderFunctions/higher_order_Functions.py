from src.py_functions import outer_function


def add(a,b): return a+b
def sub(a,b): return a-b
def multiply(a,b): return a*b


#so there will be a only one method called as operate() which will be acted as the controller method

def operate(func, a, b):

    return func(a,b)


print(operate(add,10,7))
print(operate(sub,10,7))
print(operate(multiply,10,7))



#the function can be passed as arguments as a lambda function also..

result = operate(lambda a,b: a+b+10,10,7)
print(result)

#function returning a function itself as a return value

def multipliyer(x):

    def multiply(n):

        return n*x

    return multiply


outer_function =  multipliyer(2)

print("the result is",outer_function(10))






