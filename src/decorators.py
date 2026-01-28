#Decorators will get the func as arguments add extra behaviour to it and return a new function



def mydecorator(func):

    def wrapper(username="jayadheep"):

        print("the current user is ",username)

        func()

    return wrapper



@mydecorator
def new_func():

    print("hello world")


new_func()




