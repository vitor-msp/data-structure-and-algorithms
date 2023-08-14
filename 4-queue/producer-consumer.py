#!/usr/bin/python
from threading import Thread
from queue import Queue

def producer(queue: Queue):
    print("I'm the producer")
    queue.put("test")

def consumer(queue: Queue):
    print("I'm the consumer")
    msg = queue.get()
    print(msg)

queue = Queue()

consumerThread = Thread(target=consumer, args=(queue,))
consumerThread.start()

producerThread = Thread(target=producer, args=(queue,))
producerThread.start()

consumerThread.join()
producerThread.join()