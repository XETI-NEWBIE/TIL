
####  개헷갈린다는 피드백
####### 코드로직 다시 짜보기


import sys
sys.stdin = open("special_sort.txt", "r")

T = int(input())
# 짝수 인덱스 [0][2][4][6][8]... => 가장 큰 수가 들어감 (10,9,8,7....)
# 홀수 인덱스 [1][3][5][7][9]...=> 가장 작은 수가 들어감(1,2,3,4....)
# for i / for j 문 서로 나눠서 각각 안에 if문을 넣어 검사해준다

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 일단 i 10번 반복 때려버림
    for i in range(10):
        # 기준점 설정
        special = i
        # 일단 special (최대/최소값) 이 짝수인 경우와
        if i%2 ==0:
            # i 뒤에 있는 숫자들 하나씩 확인해보기
            for j in range(i+1,N):
                # 내가 지금까지 찾은 special 후보보다 j(더 큰 값)을 발견하면?
                if arr[special]<arr[j]:
                    special=j
        # i가 홀수일 때 남은 칸에 최솟값을 채우는 방식
        else:
            # i 뒤의 값들 탐색
            for j in range(i+1,N):
                if arr[special]>arr[j]:
                    special=j

        arr[i],arr[special] = arr[special],arr[i]

    print(f'#{test_case}', *arr[:10])
