

T = int(input())
for test_case in (1, T + 1):

    N, M = map(int, input().split())
    # num = N*M
    arr = [list(map(int, input().split()))]
    # B = list((input().split()))
    # N(행), M(열)에 대해 i,j 반복문
    for i in range(N):
        for j in range(M):
            # (우, 하, 좌, 상)에 대해 방향 설정
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                # 파리의 합을 배열의 현재 위치 [i,j]으로 초기화
                pari_sum = arr[i][j]
                # M까지 포함해 c칸씩 건너 뛸 수 있도록 해준다.
                for c in range(1, M + 1):
                    # [i,j] 의 인접한 이웃 = 현재위치 + 가려는 방향 * 이동할 칸 이라고 말할 수 있다.
                    ni, nj = i + di * c, j + dj * c
                    # 만약 파리의 합이 0이고 ni가 0 이상 N 미만이고 nj가 0 이상 M 미만이라면
                    if pari_sum == 0 and 0 <= ni < N and 0 <= nj < M:
                        # pari_sum의 인접한 이웃값 [ni], [nj] 를 pari_sum에 추가해준다
                        pari_sum += arr[ni][nj]
                    else:
                        break
            print(f'#{test_case}', pari_sum)
            
            

###########################

T = int(input())
for test_case in (1, T + 1):

    N, M = map(int, input().split())
    # num = N*M
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # B = list((input().split()))
    # N(행), M(열)에 대해 i,j 반복문
    max_v = 0
    for i in range(N):
        for j in range(M):
            # (우, 하, 좌, 상)에 대해 방향 설정
            if arr[i][j] == 0:
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    # 파리의 합을 배열의 현재 위치 [i,j]으로 초기화
                    pari_sum = arr[i][j]
                    # M까지 포함해 c칸씩 건너 뛸 수 있도록 해준다.
                    # for c in range(1, M + 1):
                        # [i,j] 의 인접한 이웃 = 현재위치 + 가려는 방향 * 이동할 칸 이라고 말할 수 있다.
                    ni, nj = i + di, j + dj
                    # 만약 파리의 합이 0이고 ni가 0 이상 N 미만이고 nj가 0 이상 M 미만이라면
                    if  0 <= ni < N and 0 <= nj < M:
                        # pari_sum의 인접한 이웃값 [ni], [nj] 를 pari_sum에 추가해준다
                        pari_sum += arr[ni][nj]
                    else:
                        continue
                mav_v = max(pari_sum, max_v)
            print(f'#{test_case}', mav_v)