#!/usr/bin/python

class Stack:
    def __init__(self):
        self.__items__ = []

    def push(self, newItem):
        self.__items__.append(newItem)

    def pop(self):
        if not self.__isEmpty__(): return self.__items__.pop()

    def __isEmpty__(self):
        return len(self.__items__) == 0
    
    def clear(self):
        self.__items__ = []

stack = Stack()
stack.pop()
stack.push(2)
print(stack.__items__)
stack.push(4)
print(stack.__items__)
stack.push(7)
print(stack.__items__)
# stack.clear()
print(stack.__items__)
stack.pop()
print(stack.__items__)
stack.pop()
print(stack.__items__)
stack.pop()
print(stack.__items__)
stack.pop()
print(stack.__items__)