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

# import sys
# sys.stdin = open("numbercard.txt", "r")

# T=int(input())
# for test_case in range(1,T+1):

#     n=int(input())
#     arr=list(map(int,input()))
#     # 방은 여유있게 줘야지...
#     count=[0]*10
#     # arr의 개수만큼 돌게해줘야한다
#     for i in range(len(arr)):
#         # 미치겠다 count[i]가 아니라 count[arr[i]]였다 뭘 어디까지 떠맥여줘야대 개헷갈리네
#         count[arr[i]]+=1

#     max_num=0
#     max_count=0

#     for card in range(len(count)):
#         if count[card] >= max_count:
#             max_count=count[card]
#             # 와 레전드 이게 최대치다 뭘해야할지 도저히 생각이 나지않는다
#             max_num=card
#     print(f'#{test_case} {max_num} {max_count}')


# import sys
# sys.stdin = open("numbercard.txt", "r")

# T = int(input())
# for test_case in range(1,T+1):
    
#     n=int(input())
#     arr = list(map(int, input()))

#     count=[0]*10
#     # for i in range(n) 이라고 써줘도 된다 !!!!!!!!!!
#     # for num in arr:
#     #    count[num] += 1  이런 방식도 가능하다! (여기에선)
#     for i in range(len(arr)):
#         count[arr[i]]+=1
    
#     max_count=0
#     max_num=0

#     for card in range(len(count)):
#         if count[card]>=max_count:
#             max_count=count[card]
#             max_num = card
    
#     print(f'#{test_case} {max_num} {max_count}')

##############################################################

# 숫자카드 문제 변형 (1) : 최솟값 찾기

# import sys
# sys.stdin = open ("numbercard.txt", "r")

# T = int(input())
# for test_case in range(1,T+1):
    
#     n=int(input())
#     arr=list(map(int,input().strip()))

#     count=[0]*10
    
#     for i in range(len(arr)):
#         count[arr[i]]+=1
    
#     min_count=999
#     min_num=0

#     for card in range(len(count)):
#         # 현재 최대기록인 min_count보다 작다? 하면 바로 갱신 때리기
#         # 정리본은 Trail1.py에 상세히 기록해둠
#         # 무조건 count[card]가 기준이다. 얠 기준으로 부등호 설정이 중요
#         if count[card]>0 and count[card]<min_count:
#         # if count[card]>=max_count:
#             min_count=count[card]
#             min_num=card

#     print(f'#{test_case} {min_num} {min_count}')

## 1. if 조건문의 수정이 필요
## 2. 부등호 방향도 다시 생각해보자

##############################################################

# 숫자 카드 문제 변형 (2) : 짝수 최댓값 찾기

# import sys
# sys.stdin = open("numbercard.txt", "r")

# T=int(input())
# for test_case in range(1,T+1):
#     n=int(input())
#     arr=list(map(int, input().strip()))

#     count=[0]*10

#     # for i in range(len(arr)):로 쓰고 싶다면
#     # 반드시 if arr[i]%2==0 처럼 처리해야된다 ! 
#     #     if i%2==0: ===> (x)
#     #         count[arr[i]]+=1

#     for i in arr:
#         if i%2==0:
#             count[i]+=1

#     max_count=0
#     max_num=0

#     for card in range(len(count)):
#         if count[card]>=max_count:
#             max_count=count[card]
#             max_num=card

#     # 아래처럼 쓰는 것도 가능하다 ! 그냥 짝수 조건만 뒤로 빼주기 ㅋㅋ
#     # for i in range(len(arr))
#     #     count[arr[i]]+=1
#     # max_count=0
#     # max_num=0
#     # for card in range(len(count)):
#     #     if card%2==0 and count[card]>=max_count:
#     #         max_count=count[card]
#     #         max_num=card

#     print(f'#{test_case} {max_num} {max_count}')

##############################################################

# 숫자 카드 문제 변형 (3) : 최대 콤보 숫자/횟수 찾기

import sys
sys.stdin = open("numbercard(2).txt", "r")

T=int(input())
for test_case in range(1,T+1):

    n=int(input())
    arr=list(map(int,input().strip()))
    # combo 
    combo=1
    max_combo=1
    max_combo_num=arr[0]
    # for i in range(1,n)도 얼마든지 가능하다 !
    # 연속하는지 안하는지 파악하는 if문
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            combo+=1
        else:
            combo=1
    # 연속하는게 최댓값인지 판별하는 if문
        if combo>max_combo:
            max_combo=combo
            max_combo_num=arr[i]
    # 만약 combo가 전부 동점일 땐 가장 큰 숫자를 출력해라 ~ 뭐 이런 조건이 붙는다면?
    # 이 elif문은 그냥 투명인간임모임
        elif combo==max_combo:
            if arr[i]>=max_combo_num:
                max_combo_num=arr[i]

    print(f'#{test_case} {max_combo_num} {max_combo}')

# 최대 combo 숫자 / 횟수 출력하기

# import sys
# sys.stdin = open("numbercard(2).txt", "r")

# T=int(input())
# for test_case in range(1,T+1):
    
#     n=int(input())
#     arr=list(map(int,input().strip()))

#     combo=1
#     max_combo=1
#     #내부숫자를기록하는 것이므로 arr[0]으로 설정해야함
#     max_combo_num=arr[0]

#     for i in range(len(arr)):
#         if arr[i]==arr[i-1]:
#             combo+=1
#         else:
#             combo=1
        
#         if combo>=max_combo:
#             max_combo=combo
#             max_combo_num = arr[i]
    
#     print(f'#{test_case} {max_combo_num} {max_combo}')


# 다시쓰기 연습

import sys
sys.stdin = open("numbercard.txt", "r")

T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    arr=list(map(int, input().strip()))

    count=[0]*10

    for i in range(len(arr)):
        count[arr[i]]+=1
    
    max_count=0
    max_num=0

    for num in range(len(count)):
        # num은 0번카드, 1번카드.. 이런 인덱스 숫자번호
        # count[num]이 각 카드칸에 기록된 진짜 숫자카드 장수임
        if count[num]>=max_count:
            max_count=count[num]
            # count는 0부터 9까지가는데, 작은 수에서 큰 방향으로 셈함
            # >= 부등호 때문에 장수가 똑같다면 뒤에 나오는 숫자가 앞의 숫자를 밀어내고 자리를 뺏는 것
            # if) 같은 장수+숫자작은쪽 출력하라고 하면 걍 > 만 쓰면 된다.
            max_num=num

    print(f'#{test_case} {max_num} {max_count}')