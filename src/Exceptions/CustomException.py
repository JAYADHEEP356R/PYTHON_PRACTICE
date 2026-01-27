class customException(Exception):

    pass



num = int(input("enter the value"))


if(num<0):
    raise customException
else:
    print("no exception throwed")
