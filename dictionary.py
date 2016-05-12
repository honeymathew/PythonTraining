__author__ = 'honeymathew'

# y = {}
# y[0] = 'hello'
# y[1] = 'how r u'
# print(y[0] + ", friends")
# y["two"] = 2
# y["pi"] = 3
# print(y["two"] * y["pi"])
#print(y)

# english_to_french = {}
# english_to_french['red'] = 'rouge'
# english_to_french['blue'] = 'ble'
# english_to_french['green'] = 'vert'
# print("red in french is", english_to_french['red'])

e_to_f = {'red': 'rouge', 'blue':'ble', 'green':'vern'}
# print(len(e_to_f))
# print(list(e_to_f.keys()))
# print(list(e_to_f.values()))

# print(list(e_to_f.items()))
# del e_to_f['blue']
# print(list(e_to_f.items()))

#print('orange' in e_to_f)

# print(e_to_f.get('red', 'no'))
# print(e_to_f.get('orange', 'no'))

# x ={}
# x[0] = 'red'
# x['1']  = 'blue'
# print(x)
# y = x.copy()
# print(y)

# x = {1:'one', 2:'two'}
# y = {0:'zero', 1:'onee'}
# x.update(y)
# print(x)

sample_string = "to be or not to be i be"
count = {}
for word in sample_string.split():
    count[word] = count.get(word, 0) + 1
for word in count:
    print("the word ", word, "count is",  count[word])