#!/usr/bin/python

import heapq

queue = []

heapq.heappush(queue, (4, 'd'))
heapq.heappush(queue, (2, 'b'))
heapq.heappush(queue, (1, 'a'))
heapq.heappush(queue, (3, 'c'))

print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))
print(heapq.heappop(queue))