
import sys
sys.stdin = open('연습문제2_in.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 배열의 크기 읽기
    # 5 * 5 2차원 배열 만들기
    # 각 줄을 읽어서 숫자로 바꾼 뒤, 리스트로 묶어서 arr에 차곡차곡 쌓기
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_abs_sum=0 # 최종 값을 저장할 변수

# 모든 칸(i,j)을 주인공으로 잡고 한 칸씩 순회
    for i in range(N):
        for j in range(N):
            # 현재 칸 (i,j)의 상하좌우 방향 설정 (델타)
            # [0,-1]은 왼쪽,[1,0]은 아래, [0,1]은 오른쪽, [-1,0] 은 위
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni,nj = i+di, j+dj   # 이웃 칸의 좌표 계산
                # 벽 체크하기
                # 계산한 이웃 주소 (ni, nj)가 배열 범위 안에 있을 때만 계산
                if 0<=ni<N and 0<=nj<N:
                    # 현재 값과 이웃 값의 차이 구하기
                    diff = arr[i][j] - arr[ni][nj]
                    # 절대값 구하기 (음수면 양수로)
                    if diff < 0:
                        diff = -diff
                    # 총합에 더해주기
                    total_abs_sum += diff

    print(f'#{tc} {total_abs_sum}')
