

import sys
sys.stdin = open("min_max.txt", "r")

# ex)  (3, 29, 42, 10, 9)
# MAX-MIN 차이값 출력하기
# 양수의 개수 N이 주어진다.

# max() - min()

# N개의 양수 i 번쨰 a가 주어진다

T = int(input())
# 일단 초기화를 어떻게 하는건지 전혀 모르겠다.
# 왜 이 case에선 바구니를 비우는게 맞다는건지? 다른 데선 왜 안된다는건지.
# min_val = 1
# max_val = 1000000

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_val = numbers[0]
    min_val = numbers[0]

    for num in numbers:
        if num>max_val:
            max_val=num
        if num<min_val:
            min_val=num

    print(f'#{test_case} {max_val - min_val}')

'''
1. if vs elif : 왜 if를 두 번 쓸까?

elif를 쓰면 "위의 if가 맞으면 아래는 아예 검사도 하지 마!" 라는 뜻이 돼요. 하지만 최댓값/최솟값 문제에서는 한 숫자가 두 자격을 모두 가질 수도 있거든요.

상황: 리스트에 숫자가 딱 하나만 있는 경우 (numbers = [10])

초기화: max_val = 10, min_val = 10

if - elif 사용 시: num이 10일 때, num > max_val인지 확인하고 아니면 바로 넘어가 버려요. 만약 num < min_val인지도 확인해야 하는데, elif는 기회조차 주지 않을 수 있습니다.

if - if 사용 시: "이 숫자가 최댓값보다 커?" 확인하고, 그다음에 바로 "그건 그렇고, 혹시 최솟값보다 작기도 해?"라고 한 번 더 물어보는 거예요.

데이터가 1개일 때나 모든 숫자가 같을 때, 두 가지 조건을 모두 체크해야 오류가 없기 때문에 
if를 각각 독립적으로 쓰는 것이 정석입니다.

'''





