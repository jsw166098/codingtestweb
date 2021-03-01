# 백준-회의실

# 백준-회의실

n = int(input())

array = []

for _ in range(n):
  array.append(list(map(int, input().split())))

array_sort = sorted(array, key=lambda x: (x[1],x[0]))

print(array_sort)

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14