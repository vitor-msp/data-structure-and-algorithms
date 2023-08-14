#!/usr/bin/python
from collections import deque
from queue import Queue

queue = deque([0, 5, 6])
print(queue)
queue.append(9)
print(queue)
print(queue.popleft())
print(queue)

queue = Queue()
queue.put(1)
queue.put(4)
queue.put(9)
while not queue.empty():
    print(queue.get())