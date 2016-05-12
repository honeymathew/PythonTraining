__author__ = 'honeymathew'


def f(n, list1, list2):

    list1.append(3)
    list2 = [4, 5, 6]
    n = n + 1
    print("inside the function", n, list1, list2)


x = 5
y = [1, 2]
z = [4, 5]
f(x, y, z)
print(x, y, z)