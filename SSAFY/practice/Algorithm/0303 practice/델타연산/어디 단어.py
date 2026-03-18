import sys
sys.stdin = open("","r")

T = int(input())
for test_case in range(1,T+1):
    n, k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(n)]

    total_ans = 0 #단어가 들어갈 수 있는 총 자리 수

    di = [0,1] # 0은 가로(오른쪽), 1은 세로(아래쪽)
    dj = [1,0] # 단어는 왼쪽 -> 오른쪽, 위->아래로 세기 때문에 이 변화량만 측정

    for d in range(2):
        for i in range(n):
            for j in range(n):
                if puzzle[i][j] == 1:
                    prev_i = i - di[d]
                    prev_j = j - dj[d]

                    if not (0<=prev_i<n and 0<=prev_j<n) or puzzle[prev_i][prev_j] == 0:
                        cnt = 0
                        now_i, now_j = i,j

                        while 0<=now_i<n and 0<=now_j<n and puzzle[now_i][now_j] == 1:
                            cnt += 1
                            now_i += di[d]
                            now_j += dj[d]

                        if cnt == k:
                            total_ans+=1

    print(f'#{test_case} {total_ans}')

################

T = int(input())
for test_case in range(1,T+1):
    n,k=map(int,input().split())
    puzzle=[list(map(int,input().split())) for _ in range(n)]

    total_ans = 0

    di=[0,1]
    dj=[1,0]

    for d in range(2):
        for i in range(n):
            for j in range(n):
                if puzzle[i][j]==1:
                    prev_i = i - di[d]
                    prev_j = j - dj[d]
                    
                    if not (0<=prev_i<n and 0<=prev_j<n) or puzzle[prev_i][prev_j]==0:
                        cnt=0
                        now_i, now_j = i,j
                        
                        while 0<=now_i<n and 0<=now_j<n and puzzle[now_i][now_j]==1:
                            cnt += 1
                            now_i += di[d]
                            now_j += dj[d]

                        if cnt == k:
                            total_ans+=1

    print(f'#{test_case} {total_ans}')