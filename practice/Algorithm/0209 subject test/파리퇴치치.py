

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
            
            
'''
1. 반복문 문법 (range)

작성: for test_case in (1, T + 1): (튜플로 인식되어 1과 T+1 두 번만 돕니다)

수정: for test_case in range(1, T + 1):

2. 2차원 배열 입력 (input)

작성: arr = [list(...)] (한 줄만 읽어옵니다)

수정: arr = [list(map(int, input().split())) for _ in range(N)] (N줄을 읽어와야 합니다)

3. 핵심 로직 (인접 4방향 vs 레이저)

문제: 작성하신 코드는 c를 곱해서 멀리 있는 칸까지 더하고 있습니다.

수정: 문제의 그림을 보면 바로 옆(거리 1) 칸들만 더합니다. c 반복문은 제거해야 합니다.

4. 최대값 갱신 및 출력 위치

문제: print가 반복문 안에 있어서 계산할 때마다 출력됩니다.

수정: 모든 칸을 다 검사한 뒤, 반복문이 끝나면 가장 큰 값(max_pari)을 한 번만 출력해야 합니다.
'''

# 수정 코드 완성본

T = int(input())
for test_case in range(1, T + 1): # range 추가

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N):
        for j in range(M):
            # 트랩은 0인 칸에만 설치 가능 
            if arr[i][j] == 0: # 트랩 설치 가능한지 여부 판별
                pari_sum = 0 # 잡은 파리 버리고 0마리부터 새로 숫자 초기화
                
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < N and 0 <= nj < M:
                        pari_sum += arr[ni][nj] # 4방향의 파리 수를 차곡차곡 더함 
                
                # 4방향 다 더한 후 최대값 비교 (오타 수정)
                if pari_sum > max_v:
                    max_v = pari_sum
                    
    # 모든 칸을 다 검사한 후 마지막에 한 번만 출력! 
    print(f'#{test_case} {max_v}')

'''
(1, 1) 칸이 0일 때: 여기에 트랩을 설치하면 몇 마리 잡는지 계산해야 하죠? 이때 기존에 계산했던 값들은 다 버리고 0마리부터 새로 세기 시작해야 합니다. 그래서 pari_sum = 0으로 초기화하는 거예요.

(2, 2) 칸이 0일 때: (1, 1) 계산이 끝났으니, 다시 **새 장바구니(pari_sum = 0)**를 들고 (2, 2) 주변의 파리들을 담아야 합니다.

만약 초기화를 안 하면? (1, 1)에서 잡은 20마리에 (2, 2)에서 잡은 14마리가 더해져서 34마리라고 잘못 계산하게 됩니다.

'''
############################

# 비슷한데 다른 방법

T = int(input())

for test_case in range(1, T + 1):
    # N: 행(높이), M: 열(너비)
    N, M = map(int, input().split())
    
    # N줄에 걸쳐서 격자 정보 입력 받기 (리스트 컴프리헨션 사용)
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_pari = 0 # 이번 테스트 케이스에서 잡을 수 있는 최대 파리 수

    # 전체 격자를 순회하며 '0'인 곳(트랩 설치 가능)을 찾습니다.
    for i in range(N):
        for j in range(M):
            # 빈 칸(0)에만 트랩 설치 가능
            if arr[i][j] == 0:
                current_sum = 0 # 현재 위치에서 잡는 파리 수
                
                # 상, 하, 좌, 우 4방향 탐색
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = i + di, j + dj
                    
                    # 격자 범위 내에 있는지 확인 (범위를 벗어나면 안됨)
                    if 0 <= ni < N and 0 <= nj < M:
                        current_sum += arr[ni][nj]
                
                # 4방향을 다 더한 후, 지금까지의 최대값보다 크면 갱신
                if current_sum > max_pari:
                    max_pari = current_sum

    # 모든 탐색이 끝난 후 결과 출력
    print(f'#{test_case} {max_pari}')


###########################

