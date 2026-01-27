

try:

    num = int(input("Enter a number"))

    result = 10/num

except ZeroDivisionError:

    print("error occured")


else:

    print("operation executed succesfully")


finally:

    print("this blocks executes always")