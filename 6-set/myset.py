#!/usr/bin/python

list = [0, 1, 1, 2, 3, 3, 4]
set = set(list)
print(list)
print(set)
set.add(5)
print(set)
set.discard(2)
print(set)
# set.remove(-1)
set.clear()
print(set)

A = {0, 1, 2, 3}
B = {3, 4, 5, 6}
print(A)
print(B)
print("union")
print(A | B)
print(A.union(B))
print("intersection")
print(A & B)
print(A.intersection(B))
print("difference")
print(A - B)
print(B.difference(A))
print("symmetric difference")
print(A ^ B)
print(B.symmetric_difference(A))
print("is disjoint? " + str(A.isdisjoint(B)))
print("is disjoint? " + str({0, 1}.isdisjoint({2, 3})))