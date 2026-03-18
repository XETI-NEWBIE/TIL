# import sys
# sys.stdin = open("")
T = int(input())
for tc in range(1,T+1):
    n,m=int(input())
    maze = [list(map(int,input())) for _ in range(m)]

    start_i, start_j = 0,0
    for i in range(n):
        for j in range(m):
            if maze[i][j]==2:
                start_i, start_j = i,j

    di = [0,1,-1]  
    dj = [1,0,-0]

    ans = 0

    visited = [[0]*n for _ in range(m)]

    q = [(start_i, start_j)]
    visited[start_i][start_j] = 1

    while q:
        now_i, now_j = q.pop(0)

        if maze[now_i][now_j] == 3:
            ans = visited[now_i][now_j] - 2
            break

        for d in range(3):
            ni = now_i+di[d]
            nj = now_j+dj[d]

            if 0<=ni<n and 0<=nj<m:
                if visited[ni][nj]==0 and maze[ni][nj]!=1:
                    q.append((ni,nj))
                    visited[ni][nj] = visited[now_i][now_j]+1

    print(f'#{tc}{ans}')


########################################

# 미로 탐색 (백준)
# 원래는 0이 통로고 1이 벽, 지금은 1이 통로고 0이 벽.

n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]

di = [0,1,0,-1]       
dj = [1,0,-1,0]

visited = [[0]*m for _ in range(n)]

q = [(0,0)]
visited[0][0] = 1

while q:    
    now_i, now_j = q.pop(0)
    
    if now_i == n-1 and now_j == m-1:
        print(visited[now_i][now_j])
        break

    for d in range(4):
        ni = now_i + di[d]
        nj = now_j + dj[d]
    
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj]==0 and maze[ni][nj]==1:
                q.append((ni,nj))
                visited[ni][nj] = visited[now_i][now_j]+1
        
###################################################################

# 단지 수 구하기

n=int(input())
grid=[list(map(int,input())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

visited = [[0]*n for _ in range(n)]

all_counts= []

for i in range(n):
    for j in range(n):
        if grid[i][j]==1 and visited[i][j]==0:
            
            q=[(i,j)]
            visited[i][j]=1
            home_cnt=0

            while q:
                now_i, now_j = q.pop(0)
                home_cnt+=1

                for d in range(n):
                    ni = now_i+di[d]
                    nj = now_j+dj[d]
                    
                    if 0<=ni<n and 0<=nj<n:
                        if grid[ni][nj]==0 and visited[ni][nj]==1:
                            q.append((ni,nj))
                            visited[ni][nj]=1

            all_counts.append(home_cnt)

print(len(all_counts))

all_counts.sort()
for cnt in all_counts:
    print(cnt)

######################################

# 제미나이 문제 

n,m=map(int,input())
maze = [list(map(int,input())) for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

ans=0
visited = [[0]*m for _ in range(n)]

q = [(0,0,0)]
visited[0][0]=1

while q:
    now_i, now_j,count = q.pop(0)
    if now_i==n-1 and now_j==m-1:
        ans=count
        break
    
    for d in range(4):
        ni = now_i +di[d]
        nj = now_j+dj[d]
        
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj]==0 and maze[ni][nj]==0:
                visited[ni][nj]=1
                q.append(ni,nj,count+1)

######################################

# 미로탐색(백준) 코드 변형

n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]

di = [0,1,0,-1]       
dj = [1,0,-1,0]

visited=[[0]*m for _ in range(n)]

q = [(0,0)]
visited[0][0] =1

while q:
    now_i, now_j = q.pop(0)
    
    if now_i == n-1 and now_j == m-1:
        print(visited[now_i][now_j])
        break
    
    for d in range(4):
        ni = now_i+di[d]
        nj = now_j+dj[d]
    
        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj]==0 and maze[ni][nj]==1:
                q.append((ni,nj))
                visited[ni][nj]=visited[now_i][now_j]+1


visited=[[0]*m for _ in range(n)]

q=[(0,0)]
visited[0][0]=1

while q:
    now_i, now_j = q.pop(0)
    if now_i == n-1 and now_j == m-1:
        print(visited[now_i][now_j])
        break

    for d in range(4):
        ni = now_i+di[d]
        nj = now_j+dj[d]

        if 0<=ni<n and 0<=nj<m:
            if visited[ni][nj]==0 and maze[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj]=visited[now_i][now_j]+1
























