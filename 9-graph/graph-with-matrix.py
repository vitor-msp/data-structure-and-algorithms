#!/usr/bin/python

import numpy as np

class Graph:
    def __init__(self, oriented=True):
        self.__nodes__ = []
        self.__matrix__ = None
        self.__oriented__ = oriented

    def __expandMatrix__(self, length: int):
        matrix = self.__matrix__
        horizontal = np.zeros((length, len(matrix)), dtype=int)
        matrix = np.concatenate((matrix, horizontal), axis=0)
        vertical = np.zeros((len(matrix), length), dtype=int)
        matrix = np.concatenate((matrix, vertical), axis=1)
        self.__matrix__ = matrix

    def insertNodes(self, nodes: [str] = []):
        nodesSet = set()
        for node in nodes:
            if not node in self.__nodes__: nodesSet.add(node)
        self.__nodes__.extend(list(nodesSet))
        lenNodesSet = len(nodesSet)
        if lenNodesSet == 0: return
        if self.__matrix__ is None:
            nodesQtt = lenNodesSet
            self.__matrix__ = np.zeros(shape = [nodesQtt, nodesQtt], dtype=int)
            return
        self.__expandMatrix__(length=lenNodesSet)
    
    def __setEdges__(self, edges: [(str, str)], value: 0 | 1):
        for source, target in edges:
            sourceIndex = self.__nodes__.index(source)
            targetIndex = self.__nodes__.index(target)
            self.__matrix__[sourceIndex, targetIndex] = value
            if not self.__oriented__: self.__matrix__[targetIndex, sourceIndex] = value

    def insertEdges(self, edges: [(str, str)]):
        self.__setEdges__(edges=edges, value=1)

    def removeEdges(self, edges: [(str, str)]):
        self.__setEdges__(edges=edges, value=0)

    def removeNodes(self, nodes: [str]):
        matrix = self.__matrix__
        for node in nodes:
            try:
                index = self.__nodes__.index(node)
                matrix = np.delete(matrix, index, axis=0)
                matrix = np.delete(matrix, index, axis=1)
                del self.__nodes__[index]
            except ValueError:
                continue
        self.__matrix__ = matrix

    def containsNode(self, node: str) -> bool:
        try:
            self.__nodes__.index(node)
            return True
        except ValueError:
            return False

    def containsEdge(self, edge: (str, str)) -> bool:
        try:
            sourceIndex = self.__nodes__.index(edge[0])
            targetIndex = self.__nodes__.index(edge[1])
            return True if self.__matrix__[sourceIndex, targetIndex] == 1 else False
        except ValueError:
            return False

    def print(self):
        nodes = self.__nodes__
        msg = "   "
        for node in nodes:
            msg += "{0} ".format(node)
        print(msg)
        for index in range(0, len(nodes)):
            print(nodes[index], self.__matrix__[index])

    def __getNeighbors__(self, node: str) -> [str]:
        nodeIndex = self.__nodes__.index(node)
        nodeLine = self.__matrix__[nodeIndex]
        neighbors = []
        for index, value in enumerate(nodeLine):
            if (not index == nodeIndex) and (value == 1):
                neighbor = self.__nodes__[index]
                neighbors.append(neighbor)
        return neighbors

    def breadthFirstSearch(self, root: str) -> [str]:
        marked = []
        fifo = []
        self.__nodes__.index(root)
        marked.append(root)
        fifo.append(root)
        while len(fifo) > 0:
            node = fifo.pop(0)
            for neighbor in self.__getNeighbors__(node):
                if neighbor not in marked:
                    marked.append(neighbor)
                    fifo.append(neighbor)
        return marked

    def bfsDistAndPath(self, root: str) -> (dict, dict):
        self.__nodes__.index(root)
        dist = dict()
        dist[root] = 0
        path = dict()
        path[root] = None
        fifo = [root]
        while fifo:
            node = fifo.pop(0)
            for neighbor in self.__getNeighbors__(node):
                if neighbor not in dist:
                    dist[neighbor] = dist[node] + 1
                    path[neighbor] = node
                    fifo.append(neighbor)
        return dist, path
    
    def depthFirstSearch(self, source: str, target: str) -> bool:
        stack = [source]
        visited = []
        while stack:
            node = stack.pop()
            if node in visited: continue
            visited.append(node)
            if node == target: return True
            for neighbor in self.__getNeighbors__(node):
                if neighbor not in visited: stack.append(neighbor)
        return False

def main():
    print("===== oriented =====")
    graph = Graph(oriented=True)
    graph.insertNodes(nodes=['a', 'b', 'c'])
    graph.print()
    graph.insertEdges(edges=[('a', 'b'), ('a', 'c'), ('b', 'c')])
    graph.print()
    graph.insertNodes(nodes=['e', 'f'])
    graph.print()
    graph.insertEdges(edges=[('e', 'f')])
    graph.print()
    # graph.insertEdges(edges=[('z', 'a')])
    # graph.removeEdges(edges=[('z', 'a')])
    graph.removeEdges(edges=[('e', 'f')])
    graph.print()
    graph.removeNodes(nodes=['f', 'c'])
    graph.print()
    print("contains z?", graph.containsNode('z'))
    print("contains a?", graph.containsNode('a'))
    print("contains a->b?", graph.containsEdge(('a', 'b')))
    print("contains a->e?", graph.containsEdge(('a', 'e')))

    print("===== NOT oriented =====")
    graph = Graph(oriented=False)
    graph.insertNodes(nodes=['a', 'b', 'c'])
    graph.print()
    graph.insertEdges(edges=[('a', 'b'), ('a', 'c'), ('b', 'c')])
    graph.print()
    graph.insertNodes(nodes=['e', 'f'])
    graph.print()
    graph.insertEdges(edges=[('e', 'f')])
    graph.print()
    graph.removeEdges(edges=[('e', 'f')])
    graph.print()
    graph.removeNodes(nodes=['f', 'c'])
    graph.print()

    print("===== breadth first search =====")
    graph = Graph(oriented=False)
    graph.insertNodes(nodes=['a', 'b', 'c', 'd'])
    graph.print()
    graph.insertEdges(edges=[('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd')])
    graph.print()
    print("BFS markeds: ", graph.breadthFirstSearch(root='a'))
    dist, path = graph.bfsDistAndPath(root='a')
    print("BFS dist: ", dist)
    print("BFS path: ", path)

    print("===== depth first search =====")
    print("DFS (exists path a->d?): ", graph.depthFirstSearch(source='a', target='d'))
    print("DFS (exists path a->z?): ", graph.depthFirstSearch(source='a', target='z'))

main()