# 알고리즘 보충 IM반 문제 - 2일차

# 두 행렬의 최대 곱

# [문제 요약]
# 1. NxN 크기의 행렬 A와 MxM 크기의 행렬 B가 주어집니다 (N <= M).
# 2. 행렬 A를 행렬 B의 경계 안에서 자유롭게 움직일 수 있습니다.
# 3. A와 B가 겹치는 위치의 원소끼리 곱한 값들의 합이 '최대'가 되는 값을 구합니다.

# [풀이 전략]
# - 행렬 A가 행렬 B 위에서 움직일 수 있는 시작점(왼쪽 상단 좌표)을 (i, j)라고 합니다.
# - A가 B의 경계를 벗어나면 안 되므로, i와 j의 범위는 0부터 M - N까지입니다.
# - 모든 가능한 시작점 (i, j)에 대해 곱의 합을 구하고 최댓값을 갱신합니다.

n, m = map(int, input().split())

# 행렬 A 입력 (NxN)
matrix_a = [list(map(int, input().split())) for _ in range(n)]

# 행렬 B 입력 (MxM)
matrix_b = [list(map(int, input().split())) for _ in range(m)]

max_sum = -float('inf') # 최댓값을 아주 작은 수로 초기화

# 행렬 A의 시작 위치 (i, j)를 이동시킴
# A가 B를 벗어나지 않는 범위: 0 ~ M-N
for i in range(m - n + 1):
    for j in range(m - n + 1):
        
        # 현재 위치 (i, j)에서 두 행렬의 곱의 합 계산
        current_sum = 0
        for row in range(n):
            for col in range(n):
                # A[row][col]과 마주보는 B의 위치는 B[i + row][j + col]
                current_sum += matrix_a[row][col] * matrix_b[i + row][j + col]
        
        # 최댓값 갱신
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)


############################################################################################

# 알고리즘 보충 IM반 문제 - 3일차

# 사각형의 총 넓이  
# # 요약: N개의 직사각형 좌표가 주어질 때, 겹치는 부분을 제외한 총 넓이를 구합니다.
# 핵심 로직: 격자(2D List) 색칠하기 기법을 사용합니다. 좌표가 음수일 수 있으므로 100을 더해 인덱스를 보정합니다.
# n = int(input())
# -100~100 범위를 커버하는 200x200 도화지 생성

grid = [[0 for _ in range(200)] for _ in range(200)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 좌표 -> 인덱스 보정 (+100) 및 색칠
    for i in range(x1 + 100, x2 + 100):
        for j in range(y1 + 100, y2 + 100):
            grid[i][j] = 1

# 색칠된 칸의 합계 구하기
total_area = sum(sum(row) for row in grid)
print(total_area)

###########################################################################################


# 겹치지 않는 사각형의 넓이

# 설명: 사각형 A, B를 먼저 깔고 그 위에 사각형 M을 덮었을 때, M에 가려지지 않은 A와 B의 면적 합을 구합니다.
# 핵심 포인트:사각형 A와 B를 도화지에 1과 2로 칠합니다 (A, B는 서로 겹치지 않는다고 가정).
# 나중에 덮는 사각형 M 영역을 0으로 밀어버립니다 (덮어씌우기).
# 좌표 범위가 -1000 ~ 1000이므로 도화지 크기를 2000x2000으로 잡고 인덱스에 1000을 더해 보정합니다.

x1, y1, x2, y2 = [0] * 3, [0] * 3, [0] * 3, [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) # A
x1[1], y1[1], x2[1], y2[1] = map(int, input().split()) # B
x1[2], y1[2], x2[2], y2[2] = map(int, input().split()) # M

# 1. 2000x2000 도화지 준비 (범위 -1000 ~ 1000)
grid = [[0 for _ in range(2000)] for _ in range(2000)]
OFFSET = 1000

# 2. 사각형 A와 B를 도화지에 표시 (1로 표시)
for k in range(2): # 0은 A, 1은 B
    for i in range(x1[k] + OFFSET, x2[k] + OFFSET):
        for j in range(y1[k] + OFFSET, y2[k] + OFFSET):
            grid[i][j] = 1

# 3. 사각형 M 영역을 0으로 덮어버림 (가려진 부분 제거)
for i in range(x1[2] + OFFSET, x2[2] + OFFSET):
    for j in range(y1[2] + OFFSET, y2[2] + OFFSET):
        grid[i][j] = 0

# 4. 남은 1의 개수(면적) 세기
ans = sum(sum(row) for row in grid)
print(ans)

