# 총 테스트 케이스 개수
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    
    # 1. 인접 리스트 만들기 (1번부터 V번 노드까지 쓰기 위해 V+1 크기로 생성)
    graph = [[] for _ in range(V + 1)]
    
    # 양방향 간선 연결
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    # 출발 노드(S)와 도착 노드(G) 입력
    S, G = map(int, input().split())
    
    # 2. 방문 체크 및 '거리'를 기록할 배열
    visited = [0] * (V + 1)
    
    # 3. BFS 세팅 (import 없이 기본 리스트로 큐 구현)
    q = [S]
    visited[S] = 1 # 시작점 거리를 1로 세팅 (나중에 답 낼 때 1을 빼줍니다)
    
    ans = 0 # 도달 불가능할 경우 0을 출력하기 위한 기본값
    
    # 4. 큐가 빌 때까지 탐색 (BFS)
    while q:
        curr = q.pop(0) # 큐의 맨 앞에서 꺼냄 (FIFO)
        
        # 도착 노드(G)에 도착했다면?
        if curr == G:
            ans = visited[curr] - 1 # 시작점을 1로 시작했으니, 지나온 간선 수는 1을 빼줌
            break
            
        # 현재 노드와 연결된 이웃 노드들을 하나씩 확인
        for next_node in graph[curr]:
            # 아직 방문하지 않은 이웃이라면?
            if visited[next_node] == 0:
                q.append(next_node) # 큐에 넣고
                # 핵심! 다음 노드의 거리 = 현재 노드까지 온 거리 + 1
                visited[next_node] = visited[curr] + 1
                
    # 결과 출력
    print(f'#{tc} {ans}')