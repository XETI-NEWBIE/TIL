# BFS (Queue 사용) - 최단 거리 탐색에 최적화됨!

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 1. 시작점(2) 찾기
    start_i, start_j = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j

    # 2. 델타 방향 (우, 하, 좌, 상)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 3. 방문 체크 겸 '거리'를 기록할 배열
    visited = [[0] * N for _ in range(N)]
    
    # 4. BFS 세팅 (기본 리스트를 큐처럼 사용)
    q = [(start_i, start_j)]
    visited[start_i][start_j] = 1 # 시작점을 거리 1로 세팅

    ans = 0 # 도달 불가능할 경우 기본값 0

    while q:
        # deque의 popleft() 대신 기본 리스트의 pop(0) 사용 (FIFO)
        now_i, now_j = q.pop(0) 

        # 목적지(3)에 도착했다면?
        if maze[now_i][now_j] == 3:
            # 시작점을 1로 잡았고, 도착지 칸 자체는 제외해야 하므로 총합에서 2를 빼줌
            ans = visited[now_i][now_j] - 2
            break

        # 사방 탐색
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]

            # 범위 안이고, 벽(1)이 아니고, 아직 방문 안 한 곳이면
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and maze[ni][nj] != 1:
                    q.append((ni, nj))
                    # 핵심! 다음 칸의 거리 = 현재 칸까지 온 거리 + 1
                    visited[ni][nj] = visited[now_i][now_j] + 1

    print(f'#{tc} {ans}')


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    start_i,start_j=0,0
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                start_i,start_j=i,j

    visited = [[0]*n for _ in range(n)]

    ans=0

    q = [(start_i, start_j)]
    visited[start_i][start_j] = 1

    while q:
        now_i, now_j = q.pop(0)
        
        if maze[now_i][now_j] ==3:
            ans= visited[now_i][now_j] - 2
            break
        
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]

            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj]==0 and maze[ni][nj]!=1:
                    q.pop((ni,nj))
                    visited[ni][nj] = visited[now_i][now_j] + 1

    print(f'{tc} {ans}')

# import sys
# sys.stdin = open("")
T = int(input())
for tc in range(1,T+1):
    n=int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    
    start_i, start_j = 0,0
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                start_i, start_j = i,j

    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    ans = 0
    visited = [[0]*n for _ in range(n)]

    q = [(start_i, start_j)]
    visited[start_i][start_j]=1
    
    while q:
        now_i, now_j = q.pop(0)
        
        if maze[now_i][now_j]==3:
            ans=visited[now_i][now_j]-2
            break
        
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]

            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj]==0 and maze[ni][nj]!=1:
                    q.append((ni,nj))
                    visited[ni][nj]=visited[now_i][now_j]+1

    print(f'#{tc} {ans}')
    
            











