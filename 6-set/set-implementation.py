#!/usr/bin/python

class MySet:
    def __init__(self, list=[]):
        self.__elements__ = []
        for item in list:
            self.add(item)

    def add(self, item):
        for element in self.__elements__:
            if element == item: return
        self.__elements__.append(item)
        self.__elements__.sort()

    def remove(self, item):
        try:
            self.__elements__.remove(item)
        except ValueError:
            pass

    def clear(self):
        self.__elements__ = []
    
    def __contains__(self, item) -> bool:
        for element in self.__elements__:
            if element == item: return True
        return False

    def union(self, otherSet):
        return MySetAbs.union(self, otherSet)

    def intersection(self, otherSet):
        return MySetAbs.intersection(self, otherSet)

    def difference(self, otherSet):
        return MySetAbs.difference(self, otherSet)

    def symmetric_difference(self, otherSet):
        return MySetAbs.symmetricDifference(self, otherSet)
    
    def isdisjoint(self, otherSet) -> bool:
        return MySetAbs.isdisjoint(self, otherSet)
    
    def issubset(self, otherSet) -> bool:
        return MySetAbs.issubset(self, otherSet)

    def print(self):
        msg = "{"
        for element in self.__elements__:
            msg += "{0} ".format(element)
        msg += "}"
        print(msg)

class MySetAbs:
    def union(setA: MySet, setB: MySet) -> MySet:
        unionSet = MySet(setA.__elements__)
        for bElement in setB.__elements__:
            unionSet.add(bElement)
        return unionSet

    def intersection(setA: MySet, setB: MySet) -> MySet:
        intersectionSet = MySet()
        for aElement in setA.__elements__:
            if not setB.__contains__(aElement): continue
            intersectionSet.add(aElement)
        return intersectionSet

    def difference(setA: MySet, setB: MySet) -> MySet:
        differenceSet = MySet()
        for aElement in setA.__elements__:
            if setB.__contains__(aElement): continue
            differenceSet.add(aElement)
        return differenceSet

    def symmetricDifference(setA: MySet, setB: MySet) -> MySet:
        symDiffSet = MySet()
        newSetB = MySet(setB.__elements__)
        for aElement in setA.__elements__:
            if newSetB.__contains__(aElement):
                newSetB.remove(aElement)
                continue
            symDiffSet.add(aElement)
        for bElement in newSetB.__elements__:
            symDiffSet.add(bElement)
        return symDiffSet
    
    def isdisjoint(setA: MySet, setB: MySet) -> bool:
        intersectionSet: MySet = MySetAbs.intersection(setA, setB)
        return len(intersectionSet.__elements__) == 0
    
    def issubset(setA: MySet, setB: MySet) -> bool:
        for aElement in setA.__elements__:
            if not setB.__contains__(aElement): return False
        return True

def main():
    set = MySet([0,2,3])
    set.add(0)
    set.print()
    set.add(0)
    set.print()
    set.add(1)
    set.print()
    set.remove(0)
    set.print()
    set.remove(10)
    set.print()
    set.clear()
    set.print()

    setA = MySet([])
    setA.add(0)
    setA.add(1)
    setA.add(2)
    print("set A")
    setA.print()
    setB = MySet([])
    setB.add(2)
    setB.add(3)
    setB.add(4)
    print("set B")
    setB.print()

    print("union")
    unionSet: MySet = setA.union(setB)
    unionSet.print()
    unionSet: MySet = setB.union(setA)
    unionSet.print()

    print("intersection")
    intersectionSet: MySet = setA.intersection(setB)
    intersectionSet.print()
    intersectionSet: MySet = setB.intersection(setA)
    intersectionSet.print()

    print("difference")
    differenceSet: MySet = setA.difference(setB)
    differenceSet.print()
    differenceSet: MySet = setB.difference(setA)
    differenceSet.print()

    print("symmetric difference")
    symDiffSet: MySet = setA.symmetric_difference(setB)
    symDiffSet.print()
    symDiffSet: MySet = setB.symmetric_difference(setA)
    symDiffSet.print()

    print("is disjoint")
    print(str(setA.isdisjoint(setB))) # false
    print(str(setB.isdisjoint(setA))) # false
    print(str(MySet([0, 1]).isdisjoint(MySet([2, 3])))) # true

    print("is subset")
    print(str(setA.issubset(setB))) # false
    print(str(setB.issubset(setA))) # false
    print(str(MySet([0, 1]).issubset(MySet([0, 1, 2, 3])))) # true

main()