# sys.stdin.readline

import sys

## 문자열로 저장

str = sys.stdin.readline()

print(type(str))  ### <class 'str'>

## 다중 할당

str1, str2 = sys.stdin.readline().split()

print(str1, str2)  ### 123 123

## map 사용

num1, num2 = map(int, sys.stdin.readline().split() )
print(num1+num2)