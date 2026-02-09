

arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0

for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            for c in range(1, k+1):
                ni, nj = i+di*c, i+dj*c
                if 0<=ni<N and 0<=nj<N:
                    s+=arr[ni][nj]

