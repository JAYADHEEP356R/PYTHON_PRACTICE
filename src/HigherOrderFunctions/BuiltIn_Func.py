nums = [1,2,3,4]

result  = list(map(lambda x:x*2,nums))


print(result)


nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)


from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
print(result)
