
dx = [-1, 1,0,0]
dy = [0,0,-1,1]

x, y = 0, 0

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

graph =