# 백준 프린터 큐

import sys
from collections import deque

test_num = int(input())

for _ in range(test_num):
    N, M = sys.stdin.readline().split()
    priority =deque(map(int,sys.stdin.readline().split()))
    order = 1

    while max(deque) != deque[int(M)]:
        while max(deque) != deque[0]:
            deque.rotate(-1)

        deque.popleft()
        order += 1

    print(order)


