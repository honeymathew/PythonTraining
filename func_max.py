__author__ = 'honeymathew'

def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxi = numbers[0]
        for n in numbers[1:]:
            if n > maxi:
                maxi = n
        return maxi
print(maximum(5, 6, 3, 8, 4, 9))
