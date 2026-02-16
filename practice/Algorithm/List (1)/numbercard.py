
# ctrl + shift + f10

import sys
sys.stdin = open("number_card.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # 카드 장수 : N 입력
    N=int(input())
# N 개의 숫자를 문자열 형태로 입력
    arr=input()
# 저장소 카운팅 배열 초기화
    count = [0]*10

# 개수 세기- 입력된 문자열 순회하며 출현 횟수 누적
    for i in arr:
        count[int(i)]+=1

# 최대 개수 & 해당 숫자(인덱스)를 저장할 변수 초기화
    max_value=0
    idx_value=0

# 배열 탐색 => 최빈값 & 해당 인덱스 추출
    for j in range(len(count)):
        # 동일한 빈도 수일 경우 더 큰 숫자를 선택해야됨
        if max_value<=count[j]:
            max_value=count[j]
            idx_value=j
    # 케이스 번호 - 카드번호 - 개수 순서
    print(f'#{test_case} {idx_value} {max_value}')
