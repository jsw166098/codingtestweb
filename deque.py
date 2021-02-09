# 데크

## 회전
from collections import deque

deque = deque([1,2,3,4,5])

deque.rotate(-1)

print(deque)

# deque.rotate(1)  ## [5,1,2,3,4]
# print(deque)
#
# deque.rotate(3)  ## [2,3,4,5,1]
# print(deque)
#
# deque.rotate(-1)  ## [3,4,5,1,2]
# print(deque)
