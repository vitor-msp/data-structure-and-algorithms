#!/usr/bin/python

mydict = dict()
mydict[0] = 'zero'
mydict[1] = 'one'
mydict[2] = 'two'
print(mydict)
print(mydict[0])

mydict = dict()
mydict['zero'] = range(0, 10)
mydict['one'] = [None] * 100
mydict['two'] = {0, 1, 2}
print(mydict)
try:
    print(mydict[0])
except KeyError:
    pass
print(mydict['zero'])

for key, value in mydict.items():
    print("key: ", key)
    print("value: ", value)