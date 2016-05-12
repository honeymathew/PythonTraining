__author__ = 'honeymathew'

def fun():
    global a
    a = 1
    b = 2
    print(a,b)

a = "one"
b = "two"
fun()
print(a,b)