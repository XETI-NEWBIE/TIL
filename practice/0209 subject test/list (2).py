#
# N = int(input())
# arr=[list(map(int,input())) for _ in range(N)]
# print(*arr)
#
# arr = [[0]*4]*3
# print(arr)
# arr[0][0] = 1
# print(arr)

# arr = [[0]*4 for _ in range(3)]
#
# total=0
# for i in range(3):
#     for j in range(4):
#         total += arr[i][j]

# N * M 배열의 크기와 저장된 값이 주어질 때 합을 구하는 방법
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# s=0
# for i in range(N):
#     for j in range(M):
#         s+=arr[i][j]
#
# # 지그재그 순회
# for i in range(n):
#     for j in range(m):
#         print(array[i][j + (m-1-2*j) * (i%2)])

# 델타
#
# [상] di:-1, dj:0
#           ↑
# [좌] ← [현재 위치] → [우]
# di:0      (i, j)      di:0
# dj:-1                 dj:1
#           ↓
#        [하] di:1, dj:0

# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

# arr = [[1,2,3,4], [5,6,7,8],[9,10,11,12]]
# N=3
# M=4
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  #방법 2번
#             ni, nj = i+di, j+dj
#         # for d in range(4):      # 방법 1번
#         #     ni = i + di[d]
#         #     nj = j + dj[d]
#             if 0<=ni<N and 0<=nj<M:
#                 #  print(arr[ni][nj])

# N * N 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최댓값 (k=2)
    # k=2
    # max_v = 0
    # for i in range(N):    # 모든원소
    #     for j in range(N):  # 모든원소
    #         s = arr[i][j] # (i,j) 좌표라고 생각하면 됨
    #         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:   # 각 방향 설정 (우,하,좌,상)
    #             for c in range(1, k+1):    # 거리별. c => 내가 몇 칸 갈 것인지를 설정 k는 최대범위
    #                 ni, nj = i+di*c, j+dj*c # 현재 위치가 (i,j)면 세로로 얼만큼 (di*c), 가로로 얼만큼 (dj*c) 을 더해서 새로운 주소 계산 (ni,nj)
    #                 if 0<=ni<N and 0<=nj<N: # 단, N 이상이면 불가
    #                     s+=arr[ni][nj]
    #         if max_v<s:
    #             max_v=s
# 만약 현재 (2,2)인데 오른쪽으로 (di=0, dj=1) 2칸 (c=2) 가고 싶다면?
# ni = 2+0*2 = 2  (현재위치+좌표*칸수)
# nj = 2+1*2 = 4  (현재위치+좌표*칸수)
# 최종 도착지는 (2,4)


# 전치 행렬
# i : 행의 좌표, 행의 크기 len(arr)
# j : 열의 좌표, 열의 크기 len(arr)
# arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3행렬
# for i in range(3):
#     for j in range(3):    # for j in range(i) 인 경우엔 if문 필요 X
#         if i < j:         # i=1이라고 하면 j=
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

# # 선택 정렬
# def selection_sort(a,N):
#     for i in range(N-1):       # 정렬 구간의 첫 인덱스
#         min_idx = i            # 첫 원소를 최솟값으로 가정
#         for j in range(i+1, N): # 첫 인덱스를 최솟값으로 가정했으므로 그 다음인 i+1부터 시작
#             if a[min_idx] > a[j]: # 최솟값의 인덱스 갱신
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]  # 구간 최솟값을 구간 맨 앞으로 ㄱㄱ


# 앞에 나오는 행은 세로 이동
# 뒤에 나오는 열은 가로 이동

# [ 0, 1] : 뒤에 숫자가 있네? → 가로(열) 이동 → 오른쪽
#
# [ 0, -1] : 뒤에 마이너스가 있네? → 가로(열) 감소 → 왼쪽
#
# [ 1, 0] : 앞에 숫자가 있네? → 세로(행) 이동 → 아래쪽 (층수가 늘어나니까)
#
# [-1, 0] : 앞에 마이너스가 있네? → 세로(행) 감소 → 위쪽 (층수가 줄어드니까)


# 버블 솔트
# 배열을 활용한 버블 정렬 알고리즘 예시 (오름차순)
# def bubble sort(a,N):       # 정렬할 list, 원소 수 N
#     for i in range(N-1, 0, -1): # 범위의 끝 위치
#         for j in range(i):      # 비교할 왼쪽 원소 인덱스 j
#             if a[j]>a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#