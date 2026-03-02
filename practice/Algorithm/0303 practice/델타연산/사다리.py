import sys

# 입력 파일 읽기 (제출 시에는 주석 처리하거나 input()으로 대체)
# sys.stdin = open('input.txt', 'r')

for _ in range(10):  # 총 10개의 테스트 케이스
    tc_num = int(input())
    # 100x100 사다리 입력 받기
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 1. 도착점(2) 위치 찾기 (맨 밑 줄 r=99에서 탐색)
    now_i = 99
    now_j = 0
    for j in range(100):
        if ladder[99][j] == 2:
            now_j = j
            break
            
    # 2. 델타 설정 (좌, 우, 상 순서 - 우선순위 반영)
    di = [0, 0, -1]
    dj = [-1, 1, 0]
    
    # 방문 표시를 위한 배열 (왔던 길을 다시 돌아가지 않게 함)
    visited = [[0] * 100 for _ in range(100)]
    
    # 3. 맨 위(r=0)에 도착할 때까지 반복
    while now_i > 0:
        visited[now_i][now_j] = 1 # 현재 위치 도장 쾅!
        
        # 델타 방향 탐색 (0:좌, 1:우, 2:상)
        for d in range(3):
            nr = now_i + di[d]
            nc = now_j + dj[d]
            
            # 범위 안이고, 길이 있고(1), 가본 적 없는 곳이라면?
            # ladder[nr][nc] == 1 : 거기에 사다리 선이 그려져있나?
            # not visited[nr][nc] : 방금 내가 왔던 길이나 이미 가본 길은 아니지?
            if 0 <= nr < 100 and 0 <= nc < 100:
                if ladder[nr][nc] == 1 and not visited[nr][nc]:
                    now_i, now_j = nr, nc # 이동!
                    break # 방향 하나 결정했으면 다음 칸으로 (for문 탈출)

    print(f"#{tc_num} {now_j}")


for _ in range(10):
    test_case = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    now_i = 99
    now_j = 0
    for j in range(100):
        if ladder [99][j] == 2:
            now_j = j
            break
    
    di = [0,0,-1]
    dj = [-1,1,0]

    visited = [[0]*100 for _ in range(100)]

    while now_i>0:
        visited[now_i][now_j] = 1

        for d in range(3):
            ni = now_i + di[d]
            nj = now_j + dj[d]

            if 0<=ni<100 and 0<=nj<100:
                if ladder [nr][nc] == 1 and not visited [nr][nc]:
                    now_i, now_j = ni,nj
                    break
    
    print(f'#{test_case} {now_j}')

test_case = int(input())
ladder = [[list(map(int,input().split()) for _ in range(100))]]

now_i = 99
now_j = 0

for j in range(100):
    if ladder[99][j]==2:
        now_j=j
        break

visited = [[0]*100 for _ in range(100)]

di = [0,0,-1]
dj = [1,-1,0]

while now_i>0:
    visited[now_i][now_j] = 1
    
    for d in range(3):
        ni = now_i + di[d]
        nj = now_j + dj[d]

        if 0<=ni<100 and 0<=nj<100:
            if ladder[ni][nj] == 1 and not visited[ni][nj]:
                now_i,now_j = ni, nj
                break
            
print(f'#{test_case} {now_j}')