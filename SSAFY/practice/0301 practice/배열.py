# # 2행 4열 데이터 입력
# arr = [
#     list(map(int, input().split())),
#     list(map(int, input().split()))
# ]

# # 가로 평균 
# row_avgs = []
# for row in arr:
#     row_avgs.append(sum(row) / 4)
# print(*(f"{a:.1f}" for a in row_avgs))

# # 세로평균
# col_avgs = []
# for j in range(4):
#     col_sum = arr[0][j] + arr[1][j]
#     col_avgs.append(col_sum / 2)
# print(*(f"{a:.1f}" for a in col_avgs))

# # 전체 평균
# total_avg = (sum(arr[0]) + sum(arr[1])) / 8
# print(f"{total_avg:.1f}")

# ###################################

# # 행열 입력 
# n, m = map(int, input().split())

# # 첫 번째 격자와 두 번째 격자 데이터 입력 
# grid1 = [list(map(int, input().split())) for _ in range(n)]
# grid2 = [list(map(int, input().split())) for _ in range(n)]

# # 같은 위치의 값을 비교=> 결과 출력
# for i in range(n):
#     for j in range(m):
#         if grid1[i][j] == grid2[i][j]:
#             print(0, end=" ")
#         else:
#             print(1, end=" ")
#     print() # 한 행이 끝나면 줄바꿈

####################################################

# # 1번째 33 배열 입력 
# arr1 = [list(map(int, input().split())) for _ in range(3)]

# # 중간 빈 줄 처리
# input() 

# # 2번째 33 배열 입력
# arr2 = [list(map(int, input().split())) for _ in range(3)]

# # 같은 위치의 수끼리 곱
# for i in range(3):
#     for j in range(3):
#         # 같은 위치끼리 곱
#         print(arr1[i][j] * arr2[i][j], end=" ")
#     print() 

# ##########################

# n = int(input())
# # n x n 빈 격자
# grid = [[0] * n for _ in range(n)]

# num = 1
# # 오른쪽 열(n-1)부터 왼쪽 열(0)까지
# for j in range(n - 1, -1, -1):
#     # 열(j)과 시작 위치를 고려해서 방향 결정 
#     # 오른쪽에서 1, 3 등 홀수 열은 아래=>위
#     if (n - 1 - j) % 2 == 0:
#         for i in range(n - 1, -1, -1):
#             grid[i][j] = num
#             num += 1
#     # 오른쪽에서 2,4 등 짝수 열은 위=>아래
#     else:
#         for i in range(n):
#             grid[i][j] = num
#             num += 1

# # 격자 출력
# for row in grid:
#     print(*(row))

###############################################

# n = int(input())

# # nxn 2차원 리스트 0으로
# triangle = [[0] * n for _ in range(n)]

# for i in range(n):
#     # 시작끝 = 1로 설정
#     triangle[i][0] = 1
#     triangle[i][i] = 1
    
#     # 양 끝 사이의 숫자들 채우기 (i가 2 이상일 때부터 작동!!!!!!!!!!)
#     for j in range(1, i):
#         # 바로 위 행의 왼쪽과 오른쪽 수의 합
#         triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

# ###########################################

# for i in range(n):
#     # 각 행에서 i+1개만큼의 숫자만 출력
#     for j in range(i + 1):
#         print(triangle[i][j], end=" ")
#     print() #

# # N(격자 크기)과 M(점의 개수) 
# n, m = map(int, input().split())

# # nxn 크기 빈 리스트
# grid = [[0] * n for _ in range(n)]

# # M개의 점 위치를 입력받아 번호 표시
# for i in range(1, m + 1):
#     r, c = map(int, input().split())
#     # i => (r-1, c-1) 좌표에 저장
#     grid[r - 1][c - 1] = i

# for row in grid:
#     # 리스트 숫자 출력
#     print(*(row))

# ###################################

# # 10개의 문자열을 입력받아 리스트 생성
# words = []
# for _ in range(10):
#     words.append(input())

# # 마지막 줄에 주어지는 기준 문자 입력 
# target_char = input()

# # 변수 t/f 
# found = False

# # 마지막 문자 일치여부 확인
# for word in words:
#     # word[-1]가 기준 문자와 같다면 출력
#     if word[-1] == target_char:
#         print(word)
#         found = True

# # 일치하는 문자열이 하나도 없으면 None 
# if not found:
#     print("None")

# ##################################

# n=int(input())
# numbers="".join(input().split())
# for i in range(0, len(numbers), 5):
#     print(numbers[i:i+5])
# #################################



