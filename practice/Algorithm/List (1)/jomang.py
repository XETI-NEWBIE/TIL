

import sys
sys.stdin = open("jomang.txt", "r")

T = 10

for test_case in range(1, T + 1):
    # 건물의 개수 N 입력
    N = int(input())

    # 건물들의 높이 리스트 입력
    buildings = list(map(int, input().split()))

    # 조망권이 확보된 세대 수를 저장할 변수
    total_view = 0

    # 양 끝 2칸을 제외하고 2번 인덱스부터 N-3번 인덱스까지 반복
    for i in range(2, N - 2):
        # 현재 건물(i) 기준 왼쪽 2칸, 오른쪽 2칸 중 가장 높은 건물의 높이 찾기
        # i-2, i-1, i+1, i+2
        max_h = 0

        # 주변 4개의 건물 높이를 확인
        for j in [i - 2, i - 1, i + 1, i + 2]:
            if buildings[j] > max_h:
                max_h = buildings[j]

        # 현재 건물이 주변에서 가장 높은 건물보다 높을 경우에만 조망권이 발생
        if buildings[i] > max_h:
            # 현재 건물 높이에서 가장 높은 이웃 건물 높이를 뺀 만큼 더해쥼
            total_view += (buildings[i] - max_h)

    print(f"#{test_case} {total_view}")



# 조망권

## condition
# width <= 1000
# 맨 왼쪽 두 칸 & 맨 오른쪽 두 칸 => 건물 x
# 빌딩 height <= 255

## Testcase
# 1번째 줄에는 건물의 개수 N이 주어진다
# 2번째 줄에는 N개의 건물 높이가 주어진다
# 맨 왼쪽 두 칸 & 맨 오른쪽 두 칸 => 높이 0

## Output
# test-case 번호 출력
# 공백 후 조망권 확보된 세대 수 출력

