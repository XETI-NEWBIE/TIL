
# SWEA 파리퇴치 문제

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_flies = 0 # 가장 많이 잡은 파리 수 저장용
    
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            
            current_sum = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    current_sum += arr[x][y]
            
            if current_sum > max_flies:
                max_flies = current_sum

    print(f"#{tc} {max_flies}")

#############################

# SSAFY 변형 파리퇴치 문제

T = int(input())
for tc in range(1, T + 1):
    # 주의: 직사각형이므로 N(세로), M(가로)을 따로 받습니다.
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_flies = 0
    
    # 델타 설정 (상, 하, 좌, 우)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    # 1. 격자 전체를 순회합니다. (세로 N, 가로 M)
    for i in range(N):
        for j in range(M):
            
            # ★ 핵심 변형 포인트: 값이 0인 곳에만 설치 가능!
            if arr[i][j] == 0:
                temp_sum = 0
                
                # 2. 기준점(i, j)으로부터 상하좌우 탐색 (델타 탐색)
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    
                    # 3. 인접 칸이 격자 범위 N x M 안에 있는지 체크
                    if 0 <= ni < N and 0 <= nj < M:
                        temp_sum += arr[ni][nj]
                        
                # 4. 최댓값 갱신
                if temp_sum > max_flies:
                    max_flies = temp_sum
                    
    print(f'#{tc} {max_flies}')