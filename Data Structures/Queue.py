# a queue is a collection of items where the first item added is the first item removed (FIFO)
from collections import deque

Queue = deque(["apple", "banana", "cherry"])
print(Queue)
 
Queue.append("date")
print(Queue)    

Queue.append("elderberry")
print(Queue)

Queue.popleft()
print(Queue)