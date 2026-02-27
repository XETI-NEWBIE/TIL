# '''
# 7 8
# 4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
# '''

# def bfs(s, V):  # 시작정점 s, 마지막 정점 V
#     visited = [0] * (V+1)   # visited 생성
#     q = []          # 큐 생성
#     q.append(s)     # 시작점 인큐
#     visited[s] = 1  # 시작점 방문표시
#     while q:        # 큐에 정점이 남아있으면 front != rear
#         t = q.pop(0)    # 디큐
#         print(t)        # 방문한 정점에서 할일
#         for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
#             if visited[w]==0:
#                 q.append(w)     # w인큐, 인큐되었음을 표시
#                 visited[w] = visited[t] + 1

# V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
# arr = list(map(int, input().split()))
# # 인접리스트 -------------------------
# adj_l = [[] for _ in range(V+1)]
# for i in range(E):
#     v1, v2 = arr[i*2], arr[i*2+1]
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)    # 방향이 없는 경우
# # 여기까지 인접리스트 -----------------
# bfs(1, 7)


# 가장 기본적인 BFS 탐색
# 

'''
7 8 # 정점 수 간선수 
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s,V): #시작 정점 s, 마지막 정점 V       # 0번 정점? 이 있는지 꼭 확인해주기
    visited = [0]*(V+1) #visited 생성
    q = [s] # queue 생성
            # 시작점 enqueue (s 넣어놨으므로 해결)
    visited[s]=1 # enqueue 표시

    while q:    # queue에 남은 정점이 있으면 dequeue
        t = q.pop(0)  # dequeue해서 t에 저장
        print(t)      # dequeue한 정점 t 방문
        for w in adj_list[t]: # t에 인접하고 아직 enqueue되지 않은 정점 w가 있으면
            if visited[w] == 0:   
                q.append(w)  # w enqueue 
                visited[w] = visited[t]+1  # w enqueue 표시 (방문기록)

V,E = map(int, input().split())
arr = list(map(int, input().split()))
# adj_list(인접 리스트) i행에 i번 정점에 인접한 정점 번호 저장
adj_list = [[] for _ in range(V+1)] # V번 행까지 비어있는 행 준비
for i in range(E):
    # v1,v2 (정점 vertex)
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)     # 방향이 없는 경우에만 해당

    visited = [0]*(V+1) #visited 생성
    q = [s] # queue 생성
            # 시작점 enqueue (s 넣어놨으므로 해결)
    visited[s]=1 # enqueue 표시

    while q:    # queue에 남은 정점이 있으면 dequeue
        t = q.pop(0)  # dequeue해서 t에 저장
        print(t)      # dequeue한 정점 t 방문
        for w in adj_list[t]: # t에 인접하고 아직 enqueue되지 않은 정점 w가 있으면
            if visited[w] == 0:   
                q.append(w)  # w enqueue 
                visited[w] = visited[t]+1  # w enqueue 표시 (방문기록)


def bfs(si, sj, N):
    # 1. 큐와 방문 기록지 준비
    q = [(si, sj)]
    visited = [[0] * N for _ in range(N)] # 미로 크기만큼의 체크판
    visited[si][sj] = 1 # 시작점 방문 표시
    
    # 2. 큐에 갈 곳이 남아있는 동안 반복
    while q:
        ci, cj = q.pop(0) # 현재 위치 꺼내기
        
        # 3. 도착점(3)을 찾으면 즉시 1 반환 (성공!)
        if maze[ci][cj] == 3:
            return 1
            
        # 4. 상하좌우 4방향 델타 탐색
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            
            # 미로 범위 안이고, 벽(1)이 아니며, 가본 적 없는 곳이라면?
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append((ni, nj)) # 큐에 넣기
                    visited[ni][nj] = 1 # 방문 도장 쾅!
                    
    return 0 # 큐가 빌 때까지 못 찾으면 0 반환 (실패)

# 미로 문제 메인 코드 

# --- 실행부 ---
T = int(input()) # 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input()) # 미로 크기
    # 미로를 2차원 리스트(숫자형)로 입력받기
    maze = [list(map(int, input())) for _ in range(N)]
    
    # 시작점 '2'의 좌표 찾기
    si, sj = -1, -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break
    
    result = 0
    q = [(si, sj)]
    visited = [[0] * N for _ in range(N)] # 미로 크기만큼의 체크판
    visited[si][sj] = 1 # 시작점 방문 표시
    
    # 2. 큐에 갈 곳이 남아있는 동안 반복
    while q:
        ci, cj = q.pop(0) # 현재 위치 꺼내기
        
        # 3. 도착점(3)을 찾으면 즉시 1 반환 (성공!)
        if maze[ci][cj] == 3:
            result = 1
            
        # 4. 상하좌우 4방향 델타 탐색
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            
            # 미로 범위 안이고, 벽(1)이 아니며, 가본 적 없는 곳이라면?
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    q.append((ni, nj)) # 큐에 넣기
                    visited[ni][nj] = 1 # 방문 도장 쾅!
                    
    result = 0 # 큐가 빌 때까지 못 찾으면 0 반환 (실패)

    print(f"#{tc} {result}")

    