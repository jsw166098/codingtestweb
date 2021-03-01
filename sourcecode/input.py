# input
import sys
from collections import deque

## input()
a = input()
print(a)  ### 1

## sys.stdin.readline()
a = sys.stdin.readline()
print(a) ### 1

## input().spilt()  --> 여러개일 때는 리스트로 받는다.
b = input().split()  ### ['1', '2']

## sys.stdin.readline().split() --> 여러개일 때는 리스트로 받는다.
b = sys.stdin.readline().split()  ###['1', '2']

## 나눠서 받으면 그대로 들어간다.
b1, b2 = input().split()  ### '1' '2'
b1, b2 = sys.stdin.readline().split()  ### '1' '2'

## map 여러개 입력받을시 바로 함수 적용 -> 바로 정수형으로 입력 받음

deque = deque(map(int, sys.stdin.readline().split()))
print(deque)
