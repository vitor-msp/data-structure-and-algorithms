#!/usr/bin/python

class Node():
    __data__ = None
    __nextNode__ = None

    def __init__(self, data, nextNode):
        self.__data__ = data
        self.setNext(nextNode)

    def setNext(self, nextNode):
        self.__nextNode__ = nextNode

    def getNextNode(self):
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

    def put(self, data):
        assert self.__currQttNodes__ < self.__maxNodes__, "queue is full"
        newNode = Node(data=data, nextNode=None)
        if self.__currQttNodes__ == 0:
            self.__setFirst__(newNode)
            self.__setLast__(newNode)
        else:
            self.__getLast__().setNext(newNode)
            self.__setLast__(newNode)
        self.__incrementNodes__()

    def get(self) -> Node:
        firstNode = self.__getFirst__()
        if firstNode == None: return None
        secondNode: Node = firstNode.getNextNode()
        self.__setFirst__(secondNode)
        if secondNode == None: self.__setLast__(None)
        self.__decrementNodes__()
        return firstNode
    
    def print(self):
        msg = ""
        currentNode = self.__getFirst__()
        while not currentNode == None:
            msg += "{0} ".format(currentNode.getData())
            currentNode = currentNode.getNextNode()
        print("queue: {0}, total nodes: {1}".format(msg, self.__currQttNodes__))

    def clear(self):
        self.__setFirst__(None)
        self.__setLast__(None)
        self.__currQttNodes__ = 0

def main():
    maxNodes = 3
    queue = Queue(maxNodes=maxNodes)
    print(queue.get())
    queue.print()
    myRange = range(0, maxNodes)
    for i in myRange:
        queue.put(i)
        queue.print()
    # queue.put(1)
    # queue.clear()
    # queue.print()
    for i in myRange:
        node = queue.get()
        if not node == None: print(node.getData())
        queue.print()
    exit(0)

main()