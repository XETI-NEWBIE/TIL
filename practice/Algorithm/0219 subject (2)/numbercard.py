
# # ctrl + shift + f10

# import sys
# sys.stdin = open("number_card.txt", "r")

# T = int(input())
# for test_case in range(1, T + 1):
#     # 카드 장수 : N 입력
#     N=int(input())
# # N 개의 숫자를 문자열 형태로 입력
#     arr=input()
# # 저장소 카운팅 배열 초기화
#     count = [0]*10

# # 개수 세기- 입력된 문자열 순회하며 출현 횟수 누적
#     for i in arr:
#         count[int(i)]+=1

# # 최대 개수 & 해당 숫자(인덱스)를 저장할 변수 초기화
#     max_value=0
#     idx_value=0

# # 배열 탐색 => 최빈값 & 해당 인덱스 추출
#     for j in range(len(count)):
#         # 동일한 빈도 수일 경우 더 큰 숫자를 선택해야됨
#         if max_value<=count[j]:
#             max_value=count[j]
#             idx_value=j
#     # 케이스 번호 - 카드번호 - 개수 순서
#     print(f'#{test_case} {idx_value} {max_value}')


# 숫자카드

# T=int(input())
# for test_case in range(1,T+1):

#     n=int(input())
#     arr=list(map(int, input()))
    
#     count=[0]*10

#     for i in range(len(arr)):
#         count+=1
    
#     max_val=0
#     num_val=0
    
#     for i in range(count):
#         if max_val<=count

import sys
sys.stdin = open("numbercard.txt", "r")

T=int(input())
for test_case in range(1,T+1):

    n=int(input())
    arr=list(map(int,input()))
    # 방은 여유있게 줘야지...
    count=[0]*10
    # arr의 개수만큼 돌게해줘야한다
    for i in range(len(arr)):
        # 미치겠다 count[i]가 아니라 count[arr[i]]였다 뭘 어디까지 떠맥여줘야대 개헷갈리네
        count[arr[i]]+=1

    max_num=0
    max_count=0

    for card in range(len(count)):
        if count[card] >= max_count:
            max_count=count[card]
            # 와 레전드 이게 최대치다 뭘해야할지 도저히 생각이 나지않는다
            max_num=card
    print(f'#{test_case} {max_num} {max_count}')

























