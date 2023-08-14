#!/usr/bin/python

class Node:
    def __init__(self, data, lastNode = None, nextNode = None):
        self.__data__ = data
        self.__lastNode__ = lastNode
        self.__nextNode__ = nextNode

    def __getLast__(self):
        return self.__lastNode__

    def getNext(self):
        return self.__nextNode__
    
    def getData(self):
        return self.__data__

    def __setLast__(self, last):
        self.__lastNode__ = last

    def setNext(self, next):
        self.__nextNode__ = next

class Deque:
    def __init__(self):
        self.__last__: Node = None
        self.__first__: Node = None

    def __getLast__(self)->Node:
        return self.__last__

    def __getFirst__(self)->Node:
        return self.__first__

    def __setLast__(self, last):
        self.__last__ = last

    def __setFirst__(self, first):
        self.__first__ = first

    def pushEnd(self, data):
        lastNode = self.__getLast__()
        newNode = Node(data, lastNode=lastNode, nextNode=None)
        if self.isEmpty():
            self.__setLast__(newNode)
            self.__setFirst__(newNode)
            return
        lastNode.setNext(newNode)
        self.__setLast__(newNode)

    def pushStart(self, data):
        firstNode = self.__getFirst__()
        newNode = Node(data, nextNode=firstNode, lastNode=None)
        if self.isEmpty():
            self.__setLast__(newNode)
            self.__setFirst__(newNode)
            return
        firstNode.__setLast__(newNode)
        self.__setFirst__(newNode)

    def popEnd(self) -> Node:
        if self.isEmpty(): return None
        lastNode = self.__getLast__()
        penultimateNode: Node = lastNode.__getLast__()
        if not penultimateNode == None: penultimateNode.setNext(None)
        self.__setLast__(penultimateNode)
        if self.__getLast__() == None: self.__setFirst__(None)
        return lastNode

    def popStart(self) -> Node:
        if self.isEmpty(): return None
        firstNode = self.__getFirst__()
        secondNode: Node = firstNode.getNext()
        if not secondNode == None: secondNode.__setLast__(None)
        self.__setFirst__(secondNode)
        if self.__getFirst__() == None: self.__setLast__(None)
        return firstNode

    def print(self):
        stack = []
        currNode = self.__getFirst__()
        while not currNode == None:
            stack.append(currNode.getData())
            currNode = currNode.getNext()
        print(stack)

    def isEmpty(self):
        return self.__getLast__() == None
    
    def clear(self):
        self.__setLast__(None)
        self.__setFirst__(None)


stack = Deque()
stack.popEnd()
stack.pushEnd(3)
stack.print() # 3
stack.pushEnd(4)
stack.print() # 3 4
stack.pushEnd(5)
stack.print() # 3 4 5
stack.pushStart(2)
stack.print() # 2 3 4 5
stack.pushStart(1)
stack.print() # 1 2 3 4 5
stack.pushStart(0)
stack.print() # 0 1 2 3 4 5
# stack.clear()
# stack.print()
stack.popEnd()
stack.print() # 0 1 2 3 4
stack.popEnd()
stack.print() # 0 1 2 3
stack.popEnd()
stack.print() # 0 1 2
stack.popEnd()
stack.print() # 0 1
stack.popStart()
stack.print() # 1
stack.popStart()
stack.print()