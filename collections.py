# list is a collection of elements
print('list...')
l = [1, 2, 3, 4, 5, 6]

# iterate over list
for element in l:
    print(element)

# append at the end
l.append(7)
print(l)

# insert at index 0
l.insert(0, 0)
print(l)

# removes the first occurence of the element
l.remove(4)
print(l)

# remove the last element
l.pop()
print(l)

# remove the element at index 0
l.pop(0)
print(l)

# reverse the list
l.reverse()
print(l)


l.sort()
print(l)


# dictionary is a collection of key-value pairs
print('dictionary...')
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3


# iterate over keys
for key in d:
    print(key)

# iterate over values
for value in d.values():
    print(value)

# iterate over key-value pairs
for key, value in d.items():
    print(key, value)

# check if key exists
if 'a' in d:
    print('key exists')

# set is a collection of unique elements
print('set...')
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(5)
print(s)


# iterate over set
for elemnent in s:
    print(elemnent)

# check if element exists
if 1 in s:
    print('element exists')

# tuple is a collection of elements
print('tuple...')
t = (1, 2, 3, 4, 5, 6)


# iterate over tuple
for element in t:
    print(element)

# check if element exists
if 1 in t:
    print('element exists')

# tuple is immutable
# t[0] = 0
# print(t)

# tuple can be used as key in dictionary
d = {}
d[t] = 1
print(d)

# tuple can be used as element in set
s = set()
s.add(t)
print(s)

# tuple can be used as element in list
l = []
l.append(t)
print(l)


# list comprehension
print('list comprehension...')
l = [1, 2, 3, 4, 5, 6]

# iterate over list
for element in l:
    print(element)

# iterate over list using list comprehension
[print(element) for element in l]

# iterate over list using list comprehension and filter
[print(element) for element in l if element % 2 == 0]


# dictionary comprehension
print('dictionary comprehension...')
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3

# iterate over keys
for key in d:
    print(key)

# iterate over keys using dictionary comprehension
[print(key) for key in d]

# iterate over values
for value in d.values():
    print(value)

# iterate over values using dictionary comprehension
[print(value) for value in d.values()]

# iterate over key-value pairs
for key, value in d.items():
    print(key, value)

# iterate over key-value pairs using dictionary comprehension
[print(key, value) for key, value in d.items()]

# set comprehension
print('set comprehension...')
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# iterate over set
for element in s:
    print(element)

# iterate over set using set comprehension
[print(element) for element in s]

# iterate over set using set comprehension and filter
[print(element) for element in s if element % 2 == 0]

# tuple comprehension
print('tuple comprehension...')



# queue is a collection of elements
print('queue...')
q = []
q.append(1)
q.append(2)
q.append(3)
q.append(4)

# iterate over queue
for element in q:
    print(element)

# remove the first element
q.pop(0)
print(q)

# stack is a collection of elements
print('stack...')

# iterate over stack
for element in q:
    print(element)

# remove the last element
q.pop()
print(q)

# deque is a collection of elements
print('deque...')
from collections import Counter, deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)

# iterate over deque
for element in d:
    print(element)

# remove the first element
d.popleft()
print(d)

# remove the last element
d.pop()
print(d)

# heap is a collection of elements
print('heap...')
import heapq

# create heap
h = []
heapq.heappush(h, 1)
heapq.heappush(h, 2)
heapq.heappush(h, 3)
heapq.heappush(h, 4)

# iterate over heap
for element in h:
    print(element)

# remove the smallest element
heapq.heappop(h)
print(h)

# priority queue is a collection of elements
print('priority queue...')
from queue import PriorityQueue
pq = PriorityQueue()

# add elements
pq.put(1)
pq.put(2)
pq.put(3)
pq.put(4)

# iterate over priority queue
for element in pq.queue:
    print(element)

# remove the smallest element
pq.get()
print(pq.queue)


# defaultdict is a collection of elements

# Counter is a collection of elements
c = Counter('gallad')
print(c)

# iterate over counter
for element in c:
    print(element)

# iterate over counter
for element in c.elements():
    print(element)

# iterate over counter
for element in c.most_common():
    print(element)

# iterate over counter
for element in c.most_common(2):
    print(element)









