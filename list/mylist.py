#!/usr/bin/python

def mylist():
    mylist = ["bh", "contagem", 3, [2, "test"]]
    for item in mylist:
        print(item)
    print("======")
    
    mylist.append("last")
    print(mylist)
    
    mylist.insert(1, "one")
    print(mylist)
    
    removedItem = mylist.pop()
    print(removedItem)
    print(mylist)

    mylist.remove(3)
    print(mylist)

    numList = [1, 16, -1]
    numList.sort()
    print(numList)

    numList.reverse()
    print(numList)

    print(range(0, 10, 1))
    print(list(range(0, 10, 1)))
    print(list(range(0, 10, 2)))

    numList = [0, 1, 2]
    print(numList)
    del numList[0]
    print(numList)
    numList.remove(1)
    print(numList)
    print(numList.pop())
    print(numList)

    numList.extend([0, 1, 2])
    print(numList)

    numList = list(range(0, 10))
    print("for")
    for num in numList:
        print(num)

    print("for range")
    for num in range(0, 10):
        print(num)

    print("list comprehension")
    [print(num) for num in numList]

    print("while")
    num = 0
    while num < len(numList):
        print(num)
        num += 1

    print("enumerate")
    for index, element in enumerate(numList):
        print(index, ":", element)

    print("lambda")
    sqrt = lambda num: num ** 2
    [print(sqrt(num)) for num in numList]

mylist()