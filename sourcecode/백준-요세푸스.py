# # 백준-요세푸스
#
# ## 풀이1
# import sys
# from collections import deque
#
# N, K = map(int, sys.stdin.readline().split())
#
# list = []
# deque = deque()
#
# for i in range(N):
#     list.append(i+1)
#
#
# index = 0
# for i in range(N):
#     if i ==0:
#         index += K-1
#         deque.append(list[index])
#         del list[index]
#
#     else:
#         index = (index+(K-1))%len(list)
#         deque.append(list[index])
#         del list[index]
#
# print("<", end='')
#
# while deque:
#     if len(deque) == 1:
#         print("%d>"%deque.popleft())
#     else:
#         print("%d ,"%deque.popleft(), end='')

## 풀이 2

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

deque1 = deque()
deque2 = []

deque1 = deque([i+1 for i in range(N)])

while deque1:
    deque1.rotate(-(K-1))
    deque2.append(deque1.popleft())

print("<", end='')

for i in range(len(deque2)):
    if i == len(deque2)-1:
        print("%d>"%deque2[i], end='')
    else:
        print("%d, "%deque2[i], end='')

