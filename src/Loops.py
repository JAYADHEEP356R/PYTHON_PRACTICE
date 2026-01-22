# for loop

for i in range(1,6):

    print(i)

print("=========================")


#for loop using list

languages = ["tamil","english","malayalam","kannada","telugu"]

for i in languages:

    print(i)

print("=============================")

#nested for loop

for i in languages:

    for j in range(1,6):

        print(i,j)

print("=============================")

#while loop with break statement

count = 0

while count<5:

    print(count)
    count = count +1

    if(count==3):
        break

print("============================")






