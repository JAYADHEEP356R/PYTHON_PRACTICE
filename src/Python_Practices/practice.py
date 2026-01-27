from multiprocessing.reduction import duplicate
from unicodedata import digit

list1 = [-2 ,3 ,4 ,5 ,-6 ,7]
result = []

for i in list1:

    if i <0:
        continue
    result.append(i)

print(result)

print("===================================")

list1 = [4, 5, 6, 2, 3]

total = 0

for i in list1:
    total = total + i

avg = total / list1.__len__()

print("avg: ",avg)


result = []

for i in list1:

    if i > avg:
        result.append(i)

print(result)

print("========================================")

list1 = [2,2,3,4,5,6,6,7]
result = []


for i in range(len(list1)):
    duplicate = False

    for j in range(len(list1)):

        if(duplicate):
            break

        if i!=j and list1[i]==list1[j]:

            duplicate = True



    if not duplicate:

        result.append(list1[i])



print(result)

print("============================================")

list1 = [2,2,3,4,5,6,6,7]

result = []

for i in list1:

    if list1.count(i)<=1:

        result.append(i)


print(result)

print("============================================")

list1 = [233,45,66,234,248]
result = []


for i in list1:

    digit = []
    total = 0
    temp = i

    while temp >=1:

        dig = temp %10
        digit.append(dig)
        temp = temp//10


    for j in digit:

        total = total +j


    if total %2 == 0:
        result.append(True)

    else:
        result.append(False)



print(result)






