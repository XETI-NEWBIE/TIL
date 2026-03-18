
# 1. 전체 다 훑으면서 사방 싹 다 살피기 (파리퇴치, 지뢰찾기 유형)

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    max_val = 0
    # 1. 모든 칸 전체 다 훑어버리기
    for i in range(n):
        for j in range(n):
            # 2. 현재 내 위치(i,j)에서 사방 둘러보기
            temp_sum = arr[i][j] #일단 내 자리값 더하기
            
            for d in range(4):
                ni = i+di[d]
                nj = j+dj[d]
                # 3. 주변 칸이 판(n*n) 밖으로 나가지 않았는지 확인
                if 0<=ni<n and 0<=nj<n:
                    temp_sum += arr[ni][nj] # 조건에 맞으면 행동
            # 4. 다 둘러봤으면 최댓값 갱신
            if temp_sum>max_val:
                max_val = temp_sum
    
    print(f'#{tc} {max_val}')

###################################################################################################

# 2. 한 방향으로 뚝심있게 전진해부릴때 (달팽이 숫자 류)

T = int(input())
for tc in range(1,T+1):
    n= int(input())
    # 1. 빈 판 만들기 (0으로 꽉 채우기)
    snail = [[0]*n for _ in range(n)]

    # 2. 우, 하, 좌, 상 (달팽이는 시계방향) 
    di = [0,-1,0,1]
    dj = [1,0,-1,0]

    # 3. 시작위치와 시작방향 고정 !!!!!!!!
    i,j = 0,0
    dr = 0

    # 4. 1부터 n*n까지 숫자 싹 다 쓸 때까지 반복
    for num in range(1,n*n+1):
        snail[i][j] = num   # 현재 내 자리에 도장 쾅 하고 찍어주기

    # 5. 다음에 이동할 곳 공식 만들어주기
        ni = i+di[dr]
        nj = j+dj[dr]
    
    # 6. 앞이 낭떠러지거나, 이미 숫자가 써져있으면?
        if ni<0 or ni>=n or nj<0 or nj>=n or snail[ni][nj]!=0:
            dr = (dr+1)%4

            ni = i+di[dr]
            nj = j+dj[dr]

        i, j = ni, nj

    print(f'#{tc}')
    for row in snail:
        print(*row)

##################################################################################################

# 3. 길찾기 문제 (사다리, 미로 문제 등)

T=int(input())
for tc in range(1,T+1):
    n=10 # 10*10 판이라고 가정
    arr=[list(map(int,input().split())) for _ in range(n)]

    # 1. 방향 설정 (사다리는 우,좌,상)
    di = [0,0,-1]
    dj = [1,-1,0]

    # 현재 위치 설정
    now_i, now_j = 0,0

    # 2. 출발점 (또는 도착점) 찾기
    for j in range(n):
        if arr[n-1][j] == 2:  # 맨 아랫줄 (ex : 99(100-1))에서 '2'찾기 
            now_i, now_j = n-1,j
            break
    
    # 3. visited 방문체크 배열 만들기 (왔던 길 다시 되돌아가기 방지)
    visited = [[0]*n for _ in range(n)]

    # 4. 목적지에 도달할 때까지 무한 반복
    while now_i > 0:  # ex : 맨 윗줄(0)에 도착하면 종료
        visited[now_i][now_j] = 1  # 현재 위치 밟았다고 표시

        # 갈 수 있는 3방향으로 (delta) 탐색해보기
        for d in range(3):
            ni = now_i + di[d]
            nj = now_j + dj[d]

            # 범위 안이고, 길이 있고?
            if 0<=ni<n and 0<=nj<n:
                if arr[ni][nj] == 1 and visited[ni][nj]==0:
                    now_i, now_j = ni,nj
                    break

    print(f'#{tc} {now_j}')


#### 파리퇴치 

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n) ] 

di = [0,1,0,-1]
dj = [1,0,-1,0]

max_val=0

for i in range(n):
    for j in range(n):
        temp_sum = arr[i][j]

        for d in range(4):
            ni = i+di[d]
            nj = j+dj[d]

            if 0<=ni<n and 0<=nj<n:
                temp_sum+=arr[ni][nj]
            
            if temp_sum>max_val:
                max_val = temp_sum
print(f'#{tc} {max_val}')

####### 미로 연산

di = [0,0,1]
dj = [1,-1,0]

now_i, now_j = 0,0

for j in range(n):
    if arr[n-1][j] == 2:
        now_i, now_j = n-1,j
        break

visited = [[0]*n for _ in range(n)]

while now_i>0:
    visited[now_i][now_j] = 1

    for d in range(3):
        ni = now_i+di[d]
        nj = now_j+dj[d]

        if 0<=ni<n and 0<=nj<n:
            if arr[ni][nj]==1 and visited[ni][nj]==0:
                now_i, now_j = ni,nj
                break
print(f'#{tc} {now_j}')





