# 총 10개의 테스트 케이스가 주어지므로 10번 반복합니다. 
for _ in range(10):
    # 테스트 케이스 번호를 입력받습니다. 
    tc = int(input())
    
    N = 16

    # 16x16 크기의 미로 배열을 입력받습니다.
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
    
    # 3. 방문 체크 배열 (16x16 고정 크기)
    visited = [[0] * N for _ in range(N)]
    
    # 4. DFS 세팅
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = 1 
    
    ans = 0 # 도달 불가능을 기본값(0)으로 설정 [cite: 1]
    
    while stack:
        now_i, now_j = stack.pop()
        
        # 도착점(3)에 도착하면 정답을 1로 바꾸고 탐색 종료
        if maze[now_i][now_j] == 3:
            ans = 1
            break
            
        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]
            
            # 미로 범위(16x16) 안이고, 방문하지 않았으며, 벽(1)이 아닌 경우
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and maze[ni][nj] != 1:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1

    # 결과 출력 [cite: 1]
    print(f'#{tc} {ans}')


for _ in range(n):
    tc_num=int(input())
    n=int(input())
    maze = [[list(map(int,input()))] for _ in range(n)]
    
    start_i, start_j = 0,0
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                start_i,start_j=i,j
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    visited=[[0]*n for _ in range(n)]

    stack = [(start_i, start_j)]
    visited[start_i][start_j] = 1

    ans = 0

    while stack:
        now_i, now_j = stack.pop()

        if maze[now_i][now_j]==3:
            ans=1
            break

        for d in range(4):
            ni = now_i + di[d]
            nj = now_i + dj[d]

            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj]==0 and maze[ni][nj]!=1:
                    stack.append((ni,nj))
                    visited[ni][nj]=1

    print(f'{tc_num}{ans}')