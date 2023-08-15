#!/usr/bin/python

class Node:
    def __init__(self, value = None):
        self.__right__ = None
        self.__left__ = None
        self.__value__: int = value

    def getValue(self) -> int:
        return self.__value__

    def getLeft(self):
        return self.__left__

    def getRight(self):
        return self.__right__

    def setLeft(self, newLeft):
        self.__left__ = newLeft

    def setRight(self, newRight):
        self.__right__ = newRight

class BinaryTree:
    def __init__(self, rootValue = None):
        self.__root__ = Node(value=rootValue)

    def insert(self, value: int):
        def analyseTree(root: Node, newNode: Node):
            if newNode.getValue() < root.getValue():
                if root.getLeft() is None: return root.setLeft(newNode)
                return analyseTree(root=root.getLeft(), newNode=newNode)
            if newNode.getValue() > root.getValue():
                if root.getRight() is None: return root.setRight(newNode)
                return analyseTree(root=root.getRight(), newNode=newNode)
        analyseTree(root=self.__root__, newNode=Node(value))

    def __inOrder__(self, function):
        def analyseTree(root: Node, function):
            leftNode: Node = root.getLeft()
            if not leftNode is None: analyseTree(root=leftNode, function=function)
            function(root.getValue())
            rightNode: Node = root.getRight()
            if not rightNode is None: analyseTree(root=rightNode, function=function)
        analyseTree(root=self.__root__, function=function)

    def getNodesInOrder(self) -> [int]:
        orderedNodes: [int] = []
        def returnValue(value: int):
            orderedNodes.append(value)
        self.__inOrder__(function=returnValue)
        return orderedNodes

    def __increment__(self):
        self.__currentHeight__ += 1
        if self.__currentHeight__ > self.__maxHeight__: self.__maxHeight__ = self.__currentHeight__

    def __decrement__(self):
        self.__currentHeight__ -= 1

    def getHeight(self) -> int:
        self.__maxHeight__ = self.__currentHeight__ = 0
        def analyseTree(root: Node):
            if not root.getLeft() is None:
                self.__increment__()
                analyseTree(root=root.getLeft())
            if not root.getRight() is None:
                self.__increment__()
                analyseTree(root=root.getRight())
            self.__decrement__()
        analyseTree(root=self.__root__)
        return self.__maxHeight__

    def getNodesCount(self) -> int:
        self.__nodesCount__ = 0
        def countNode(value: int):
            self.__nodesCount__ += 1
        self.__inOrder__(function=countNode)
        return self.__nodesCount__
    
    def getMinValue(self) -> int:
        def analyseTree(root: Node):
            if root.getLeft() is None: return root.getValue()
            return analyseTree(root=root.getLeft())
        return analyseTree(root=self.__root__)
    
    def find(self, value):
        def analyseTree(root: Node, value):
            if value == root.getValue(): return value
            if value < root.getValue():
                if root.getLeft() is None: return None
                return analyseTree(root=root.getLeft(), value=value)
            if value > root.getValue():
                if root.getRight() is None: return None
                return analyseTree(root=root.getRight(), value=value)
            return None
        return analyseTree(root=self.__root__, value=value)

def main():
    binaryTree = BinaryTree(rootValue=5)
    binaryTree.insert(3)
    binaryTree.insert(8)
    binaryTree.insert(5)
    binaryTree.insert(20)
    binaryTree.insert(0)
    print("nodes in order: ", binaryTree.getNodesInOrder())
    print("tree height: ", binaryTree.getHeight())
    print("nodes count: ", binaryTree.getNodesCount())
    print("min value: ", binaryTree.getMinValue())
    print("find 3:", binaryTree.find(3))
    print("not find 15:", binaryTree.find(15))
    
main()