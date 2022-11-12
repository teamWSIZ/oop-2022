from collections import deque

w = deque([1, 2, 3])

for a in w:
    if a == 2:
        w.append(71)
