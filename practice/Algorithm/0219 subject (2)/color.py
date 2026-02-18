
'''
💡 채원아, 시험장에서 멘붕 오면 이것만 기억해

1. 초기화: 

grid = [[0] * 가로 for _ in range(세로)] (가세세가! 가로가 먼저 곱해지고 세로가 뒤에!)

2. 색칠 : 

range(r1, r2 + 1) (뒤에 +1 안 붙이면 한 줄 덜 칠해져서 광탈이야!)

3. 체크: if grid[i][j] != 3 

(보라색 숫자가 3인지 7인지 30인지 문제 지문을 다시 읽어!)
'''

# import sys
# sys.stdin = open("color.txt", "r")

# T=int(input())
# for test_case in range(1,T+1):
#     n=int(input())
#     # 10*10 짜리 거대한 격자 빈 도화지 생성하기 (0으로 초기화)
#     grid = [[0]*10 for _ in range(10)]
#     # 각 TC별 우리가 칠해야할 사각형의 개수 (2개,3개 등...)
#     for _ in range(n):
#         r1,c1,r2,c2,color=map(int,input().split())
#         # i부터 j까지 돌면서 하나의 사각형을 그림 (빨강, 파랑...)
#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 grid[i][j]+=color
    
#     purple_count=0
#     # for i in range(len(grid))
#     for i in range(10):
#         # for j in range(len(grid[i]))
#         for j in range(10):
#             if grid[i][j]==3:
#                 purple_count+=1

#     print(f"#{test_case} {purple_count}")

# r1, c1, r2, c2, color 순으로 주어지는데 이게 22441이라고 하면
# 2,  2,  4,  4,    1
# 좌표 자체는 r1,c1부터 r2,c2 까지라고 표현할 수 있지만
# 사실상 r1(2) ~ r2(4) 세로줄(i) 부터 표현하고 
# 그 안을 c1(2) ~ c2(4) 가로줄 (j)이 하나씩 돌면서 각 칸을 채우는 방식이 가장 깔끔

# import sys
# sys.stdin = open("color.txt", "r")

# T=int(input())
# for test_case in range(1,T+1):
    
#     n=int(input())
#     # grid의 범위를 헷갈렸다......유유유윳
#     grid = [[0]*10 for _ in range(10)]

#     for _ in range(n):
#         r1,c1,r2,c2,color = map(int, input().split())

#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 grid[i][j]+=color
    
#     purple_count=0
#     for i in range(10):
#         for j in range(10):
#             if grid[i][j]==3:
#                 purple_count+=1
    
#     print(f'#{test_case} {purple_count}')

# 다시쓰기
# import sys
# sys.stdin = open("color.txt", "r")

# T=int(input())
# for test_case in range(1,T+1):
#     n=int(input())
#     grid=[[0]*10 for _ in range(10)]

#     for _ in range(n):
#         r1,c1,r2,c2,color=list(map(int, input().split()))
    
#     purple_count=0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j]==3:
#                 purple_count+=1
    
#     print(f'#{test_case} {purple_count}')

############################################################################################


# 색칠하기 변형 (1) : "같은 색깔끼리도 겹칠 수 있다" 는 조건으로 변경

import sys
sys.stdin = open("color.txt", "r")

T=int(input())
for test_case in range(1,T+1):
    
    n=int(input())
    grid=[[0]*10 for _ in range(10)]
    
    for _ in range(n):
        r1,c1,r2,c2,color=list(map(int,input().split()))

        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                # 1. 가장 쉬운 방법 (색깔없으면 걍 칠해주기 ㅋㅋ)
                # if grid[i][j]!=color:
                #     grid[i][j]+=color
                # 2. 가장 디테일한 방법(색깔별로 조건 나눠주기)
                # if color==1:
                #     if grid[i][j]==0 or grid[i][j]==2:
                #         grid[i][j]+=1
                # elif color==2:
                #     if grid[i][j]==0 or grid[i][j]==1:
                #         grid[i][j]+=2
                # 3. 1의 방법에 조건 추가해주기
                # grid에 color가 있거나, grid 칸이 3이라면 색칠하지마  
                if grid[i][j]!=color and grid[i][j]!=3:
                    grid[i][j]+=color

    purple_count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==3:
                purple_count+=1
    
    print(f'#{test_case} {purple_count}')

# 다시쓰기 연습
# import sys
# sys.stdin = open("color.txt", "r")

# T=int(input())
# for test_case in range(1,T+1):
#     n=int(input())
#     grid=[[0]*10 for _ in range(10)]

#     for _ in range(n):
#         r1,c1,r2,c2,color=list(map(int,input().split()))

#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 if grid[i][j]!=color and grid[i][j]!=3:
#                     grid[i][j]+=color
        
#     purple_count=0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j]==3:
#                 purple_count+=1
#     print(f'#{test_case} {purple_count}')

############################################################################################

# 색칠하기 변형 (2) : 순수한 빨간색/파란색의 넓이 구하기

import sys
sys.stdin = open("color.txt", "r")

T=int(input())
for test_case in range(1,T+1):
    
    n=int(input())
    grid=[[0]*10 for _ in range(10)]
    
    for _ in range(n):
        r1,c1,r2,c2,color=list(map(int,input().split()))
        
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                # 해당 턴의 색(빨/파)이 없거나 보라색이 아니라면? 해당 턴의 색(빨/파)을 더해준다
                # 근데 순수한 빨강 + 순수한 파랑 칸의 값의 합을 구해버렸다 ;;;;;;
                if grid[i][j]!=color and grid[i][j]!=3:
                    grid[i][j]+=color

    red_count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                red_count+=1
    print(f'#{test_case} {red_count}')

#######################################################################################

# 색칠하기 변형 (3) : 빨(1)파(2)노(4) 세 영역 합 or 두 개만 겹친 곳 합 구하기

import sys
sys.stdin = open("color.txt", "r")

T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    grid= [[0]*10 for _ in range(10)]

    for _ in range(n):
        r1,c1,r2,c2,color=list(map(int, input().split()))
        
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
            # 아직 색깔 3개 다 안 모인 칸들까지만 색칠해라 ~
            # !=color : 아직 해당 색이 안 칠해졋으면 칠해줘라~ 라는 코드
            # ex) 빨강(1)을 칠한다치면 최대 파랑(2)+노랑(4)가 섞인 칸까지만 칠할수잇듬
                if grid[i][j]!=color and grid[i][j]<7:
                    grid[i][j]+=color
    
    all_three=0
    only_two=0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==7:
                all_three+=1
            # 아래 방식으로도 되지만.. 역시 in이 제일 편하다
            # elif grid[i][j] == 3 or grid[i][j] == 5 or grid[i][j] == 6:
            # only_two += 1
            # elif grid[i][j] in {3, 5, 6}:
            # only_two += 1
            elif grid[i][j] in [3,5,6]:
                only_two+=1
    print(f'#{test_case} {all_three}')


############################################################################################

# 색칠하기 변형 (4) : 가변형 도화지 색칠하기 (h:행, w:열)

import sys
sys.stdin = open("color.txt", "r")

T=int(input())
for test_case in range(1,T+1):

    h,w=map(int, input().split())
    n=int(input())
    # 2차원배열 무조건이야 그리드 크기 (가로*세로)
    grid=[[0]*w for _ in range(h)]
    
    for _ in range(n):
        # 와 color빼먹었네 실화냐
        r1,c1,r2,c2,color = list(map(int,input().split()))
        
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if grid[i][j]!=color and grid[i][j]!=3:
                    grid[i][j]+=color
    purple_count=0
    # 실화냐고 len(h), len(w) 이렇게 쓰면 누가 알아먹는데?
    # len(grid): len(grid[i]) 그대로 써줘도 된다며
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==3:
                purple_count+=1
    print(f'#{test_case} {purple_count}')