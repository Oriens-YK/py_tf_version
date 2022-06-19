from collections import deque
import json
# arr = []

# arr.append(18168415)
# arr.append(2186168)
# dict1 = {'a':str(list(arr))}
# jsonStr  = json.dumps(dict1)
# print(dict1)
# print(jsonStr)
# dict1 = json.loads(jsonStr)
# print(dict1['a'], type(dict1['a']))
# print(dict1['a'][1:-1])
# a = dict1['a'][1:-1].split(',')
# print(a)
# q1 = deque()
# q1.append(dict1)
# print(q1)
# q1.append(dict1)
# print(q1)
# print(type(q1[0]))

# q1 = deque()
# q1.append('x')
# q1.append('y')
# q1.append('z')
# q1.append('a')
# print("Queue after enqueue operation")
# print(q1)
# q1.popleft()
# q1.popleft()
# q1.popleft()
# q1.popleft()
# print("\nQueue after dequeue operation")
# print(q1)
# https://www.delftstack.com/zh-tw/howto/python/python-queue-implementation/
from queue import Queue
q1 = Queue(maxsize = 4)
# Now adding elements to queue
q1.put('x')
q1.put('y')
q1.put('z')
q1.put('a')
print("Is the queue empty?", q1.empty())
print(q1)
#Now removing elements from queue
print(q1.get())
q1.get()
q1.get()
q1.get()
print("Is the queue empty now?", q1.empty())
print(q1)

