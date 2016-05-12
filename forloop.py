__author__ = 'honeymathew'

# x = [1.0, 2.0, 3.0]
# for i in x:
# print(1/i)

# x = [2, 3, -3, 6, 8]
# for i in range(len(x)):
#     if x[i] < 0:
#         print("negative number at position",i)

#print(list(range(10,2,-1)))

# x = range(1,10)
# print(x)

#print(range(1, 7))   #list keyword is used in actual code

# y =list(range(2,10))
# print(y)

# some_list = [(1,2,), (3, 7), (9, 5)]
# result = 0
# for t in some_list:
#     result = result + (t[0] * t[1])
#     print(result)

# some_list = [(1,2,), (3, 7), (9, 5)]
# result = 0
# for x,y in some_list:
#     result = result + (x * y)
#     print(result)
#

x = [1, 3, -5, 8, -4, 9]   #enumerate function return tuple of(index,item)
for i, n in enumerate(x):
    if n < 0:
        print("negative number at", i)