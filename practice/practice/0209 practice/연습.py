
# 코드트리 연습 Trail 0 . Chapter 9 ~

# for j in range(1):
#     print('*', end=' ')
# print()

# for j in range(5):
#     print('*', end=' ')

# # 1, 2, 3, 4 모두 자유롭게 넣을 수 있다
# for j in range(1):
#     print('*', end=' ')
# print()

# for j in range(2):
#     print('*', end= ' ')
# print()


# # # 내부 반복문에 현재 줄 번호(i)를 이용하면 반복 횟수 조절 가능
n = 4

for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
    
# # 외부 for문 : 한 행(row)을 제어
# # 내부 for문 : 한 열(column)의 수를 제어

# # 역삼각형 출력
# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()
    
    
# # # 가운데 정렬된 삼각형
# n=5
# # 몇 층으로 쌓을지를 결정
# # 1부터 n+1까지 순차적으로 증가 (층수 결정)
# for i in range(1, n+1):
#     # 왼쪽 공백 밀기
#     # 전체 층수(n) - 현재 층수(i) 만큼 공백을 출력한다
#     # 전체 층수 (n) - 현재 층수(i)이 각 층의 공백 수 
#     for j in range(n-i):
#         print(" ", end=" ")
#     # 홀수 개수로 별을 찍는 구간 (피라미드 모양 : 1, 3, 5, 7, 9)
#     # 피라미드 형태를 위해 홀수 개수로 증가한다 (2*i -1)
#     for j in range(2*i-1):
#         print("*", end=" ")
#     print()


# 아래 식의 " "의 공백을 냅두냐 / 늘리느냐에 따라서 삼각형의 모양이 바뀜
# " " : 중앙정렬 삼각형
# "" : 역삼각형 정반대로 뒤집은 형태
# "  " : 역삼각형 대각선으로 뒤집은 형태
# n = 5
# for i in range (1, n+1):
#     print("  " * (n-i) + "*" * (2 * i -1))

# 하트 찍기
# for y in range(15,-15,-1):
#     row = []
#     for x in range(-30, 30, 1):
#         x/=15
#         y/=10
#         formula = (x*x + y*y - 1)**3 - x*x*y*y*y
#         if formula <= 0:
#             row.append('*')
#         else:
#             row.append(' ')
#         x *= 15
#         x *= 10
#     print(''.join(row))

# # n = int(input())

# for i in range(n,0,-1):
#     for j in range(i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()
    
# # 이건 어떤 형태일까요옹
for i in range(n,0,-1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()
    
# # 별표 출력하기 2
# # 정수 N의 값
    
# 간단한 스택 구현은 할 줄 알아야

N = int(input())
for i in range(1, N+1):
    for j in range(2*i-1):
        print("*", end="")
    print()    