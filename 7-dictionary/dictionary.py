#!/usr/bin/python

class Dictionary:
    def __init__(self):
        self.__keys__ = []
        self.__values__ = []

    def add(self, newKey, newValue):
        for key in self.__keys__:
            if key == newKey: return
        self.__keys__.append(newKey)
        self.__values__.append(newValue)

    def remove(self, key):
        try:
            index = self.__keys__.index(key)
            del self.__keys__[index]
            del self.__values__[index]
        except ValueError:
            pass

    def get(self, key):
        try:
            index = self.__keys__.index(key)
            return self.__values__[index]
        except ValueError:
            return None

    def clear(self):
        self.__keys__ = []
        self.__values__ = []

    def keys(self):
        return self.__keys__

    def values(self):
        return self.__values__

    def items(self):
        items = []
        totalItems = len(self.__keys__)
        for index in range(0, totalItems, 1):
            keyValue = (self.__keys__[index], self.__values__[index])
            items.append(keyValue)
        return items
    
    def print(self):
        msg = "dict("
        for key, value in self.items():
            msg += "{"
            msg += "'{0}': '{1}'".format(key, value)
            msg += "}, "
        msg += ")"
        print(msg)

def main():
    dictionary = Dictionary()
    dictionary.add(0, 'zero')
    dictionary.add(1, 'one')
    dictionary.add(2, 'two')
    dictionary.print()
    print(dictionary.get(0))

    dictionary = Dictionary()
    dictionary.add('zero', range(0, 2))
    dictionary.add('one', [None] * 3)
    dictionary.add('two', {0, 1, 2})
    dictionary.print()
    print(dictionary.get(0))
    print(dictionary.get('zero'))
    print("keys", dictionary.keys())
    print("values", dictionary.values())
    for key, value in dictionary.items():
        print("key: ", key)
        print("value: ", value)
    dictionary.clear()
    dictionary.print()

main()