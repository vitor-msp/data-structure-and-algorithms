#!/usr/bin/python

class Node():
    __data__ = None
    __nextNode__ = None

    def __init__(self, data):
        self.__data__ = data

    def setNext(self, nextNode):
        self.__nextNode__ = nextNode

    def getNext(self):
        return self.__nextNode__
    
    def getData(self):
        return self.__data__

class Queue():
    __first__: Node = None
    __last__: Node = None
    __maxNodes__: Node = 10
    __currQttNodes__: Node = 0
    
    def __init__(self, maxNodes = 10):
        self.__maxNodes__ = maxNodes

    def __getFirst__(self) -> Node:
        return self.__first__

    def __getLast__(self) -> Node:
        return self.__last__

    def __setFirst__(self, first: Node):
        self.__first__ = first

    def __setLast__(self, last: Node):
        self.__last__ = last

    def __incrementNodes__(self):
        self.__currQttNodes__ += 1

    def __decrementNodes__(self):
        self.__currQttNodes__ -= 1

    def __isFull__(self)->bool:
        return self.__currQttNodes__ == self.__maxNodes__

    def isEmpty(self)->bool:
        return self.__currQttNodes__ == 0

    def put(self, data):
        newNode = Node(data)
        if self.__currQttNodes__ == 0:
            newNode.setNext(newNode)
            self.__setFirst__(newNode)
            self.__setLast__(newNode)
            self.__incrementNodes__()
            return
        self.__getLast__().setNext(newNode)
        self.__setLast__(newNode)
        if self.__isFull__():
            secondNode = self.__getFirst__().getNext()
            newNode.setNext(secondNode)
            self.__setFirst__(secondNode)
        else:
            firstNode = self.__getFirst__()
            newNode.setNext(firstNode)
            self.__incrementNodes__()

    def get(self) -> Node:
        assert self.__currQttNodes__ > 0, "queue is empty"
        firstNode = self.__getFirst__()
        self.__decrementNodes__()
        if self.__currQttNodes__ == 0:
            self.__setFirst__(None)
            self.__setLast__(None)
            return firstNode
        secondNode: Node = firstNode.getNext()
        self.__getLast__().setNext(secondNode)
        self.__setFirst__(secondNode)
        return firstNode
    
    def print(self):
        msg = ""
        loop  = True
        if self.isEmpty(): loop = False
        firstNode = currentNode = self.__getFirst__()
        while loop:
            msg += "{0} ".format(currentNode.getData())
            currentNode = currentNode.getNext()
            if currentNode == firstNode: break
        print("queue: {0}, total nodes: {1}".format(msg, self.__currQttNodes__))

    def clear(self):
        self.__setFirst__(None)
        self.__setLast__(None)
        self.__currQttNodes__ = 0

def main():
    maxNodes = 3
    queue: Queue = Queue(maxNodes=maxNodes)
    # queue.get()
    queue.print()
    for i in range(0, maxNodes + 2):
        queue.put(i)
        queue.print()
    # queue.clear()
    queue.print()
    while not queue.isEmpty():
        node = queue.get()
        if not node == None: print(node.getData())
        queue.print()
    exit(0)

main()