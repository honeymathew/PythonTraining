__author__ = 'honeymathew'

# x = [1, 2, 3, 4, 5]
# x_square = []
# for i in x:
#    x_square.append(i * i)
# print(x_square)

#list comprehension(short cut for above operation)
# x = [1, 2, 3, 4, 5, 7]
# x_square = [i * i for i in x]
# print(x_square)

#list comprehension with if
# x = [1, 2, 3, 4, 5, 7]
# x_square = [i * i for i in x if i > 3 ]
# print(x_square)

#dictionary comprehension
x = [3, 5, 7]
x_square = {i:i * i for i in x}
print(x_square)