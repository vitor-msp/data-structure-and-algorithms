#!/usr/bin/python

class Node:
    __data__ = None
    __lastNode__ = None

    def __init__(self, data, lastNode):
        self.__data__ = data
        self.__lastNode__ = lastNode

class Stack:
    def __init__(self):
        self.__top__: Node = None

    def push(self, data):
        newNode = Node(data=data, lastNode=self.__top__)
        self.__top__ = newNode

    def pop(self) -> Node:
        if self.__isEmpty__(): return
        topNode = self.__top__
        newTop = topNode.__lastNode__
        self.__top__ = newTop
        return topNode.__data__

    def print(self):
        stack = []
        nextNode = self.__top__
        while not nextNode == None:
            stack.append(nextNode.__data__)
            nextNode = nextNode.__lastNode__
        stack.reverse()
        print(stack)

    def __isEmpty__(self):
        return self.__top__ == None
    
    def clear(self):
        self.__top__ = None


stack = Stack()
stack.pop()
stack.push(2)
stack.print()
stack.push(4)
stack.print()
stack.push(7)
stack.print()
# stack.clear()
stack.print()
print(stack.pop())
stack.print()
print(stack.pop())
stack.print()
print(stack.pop())
stack.print()
print(stack.pop())
stack.print()