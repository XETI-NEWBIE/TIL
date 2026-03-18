# DFS 사용 (STACK)
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 띄어쓰기 없는 숫자를 1개씩 쪼개서 2차원 리스트로 만들기
    maze = [list(map(int, input())) for _ in range(N)]
    
    # 1. 시작점(2) 찾기
    start_i, start_j = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j
                
    # 2. 델타 방향
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    
    # 3. 방문 체크 배열 (갔던 길 또 가서 무한루프 도는 것 방지!)
    visited = [[0] * N for _ in range(N)]
    
    # 4. DFS 세팅 (Stack 사용)
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = 1 # 시작점 방문 도장!
    
    ans = 0 # 정답 (기본값 0)
    
    while stack: # 스택에 갈 곳이 남아있는 동안 계속 반복
        now_i, now_j = stack.pop() # 가장 최근에 저장한 길부터 꺼냄 (LIFO)
        
        # 목적지(3)에 도착했으면? 정답을 1로 바꾸고 탐색 종료!
        if maze[now_i][now_j] == 3:
            ans = 1
            break
            
        # 델타로 사방 탐색
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]
            
            # 미로 범위 안이고, 방문한 적 없고, 벽(1)이 아니라면?
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and maze[ni][nj] != 1:
                    stack.append((ni, nj)) # 스택에 다음 갈 곳 저장!
                    visited[ni][nj] = 1    # 방문 예약 도장 쾅!

    print(f'#{tc} {ans}') 

###############################################################################################

# BFS 사용 (Queue)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    
    start_i, start_j = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_i, start_j = i, j
                
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    
    visited = [[0] * N for _ in range(N)]
    
    # 4. BFS 세팅 (Queue 사용)
    q = [(start_i, start_j)]
    visited[start_i][start_j] = 1 
    
    ans = 0
    
    while q: # 큐에 갈 곳이 남아있는 동안
        now_i, now_j = q.pop(0) # ★ DFS와 유일하게 다른 점! 맨 처음에 넣은 걸 꺼냄 (FIFO)
        
        if maze[now_i][now_j] == 3:
            ans = 1
            break
            
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]
            
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and maze[ni][nj] != 1:
                    q.append((ni, nj)) # 큐에 다음 갈 곳 꼬리물기!
                    visited[ni][nj] = 1

    print(f'#{tc} {ans}') 




# DFS 사용 (STACK)
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # 띄어쓰기 없는 숫자를 1개씩 쪼개서 2차원 리스트로 만들기
    maze = [list(map(int, input())) for _ in range(n)]
    # 시작점 만들기
    start_i,start_j = 0,0
    
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                start_i, start_j = i,j
    # 델타 세팅
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 방문 세팅
    visited = [[0]*n for _ in range(n)]
    # dfs 세팅
    stack = [((start_i, start_j))]
    visited[start_i][start_j] = 1
    # 정답 맨들기
    ans = 0
    # while문 돌리면서 스택 탐색
    while stack:
        now_i, now_j = stack.pop() # 가장 최근에 저장한 길부터 pop()
        # 목적지가 3이면 탐색 종료
        if maze[now_i][now_j] == 3:
            ans=1
            break
        # 사방 탐색
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]
            # 미로범위 안이고 방문한적없고 벽이 아니면
            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj]==0 and maze[ni][nj]!=1:
                    stack.append((ni,nj)) #스택에 다음 갈 곳 저장
                    visited[ni][nj]==1 # 방문예약도장
    print(f'#{tc} {ans}') 



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    start_i,start_j=0,0
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                start_i, start_j = i,j
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    visited = [[0]*n for _ in range(n)]

    q = [(start_i, start_j)]
    visited[start_i][start_j]=1

    ans = 0

    while q:
        now_i, now_j = q.pop(0)
        
        if maze[now_i][now_j] == 3:
            ans=1
            break

        for d in range(4):
            ni = now_i+di[d]
            nj = now_j+dj[d]
        
            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj]==0 and maze[ni][nj]!=1:
                    q.append((ni,nj))
                    visited[ni][nj]=1

    print(f'#{tc}{ans}')