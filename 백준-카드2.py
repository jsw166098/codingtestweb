# 백준 카드2
import sys
from collections import deque

input = int(sys.stdin.readline())

deq = deque()

for num in range(input):
    deq.append(num+1)

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq.popleft())


