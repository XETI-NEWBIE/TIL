

import sys
sys.stdin = open("text_length.py", "r")
# 최대 / 최소 빈도 글자수 비교
# length
# 딕셔너리 사용법: count += 1이 아니라 count[char] += 1처럼 어떤 칸(이름표)의 숫자를 올릴지 정확히 찍어주기!
T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
# count는 딕셔너리. 딕셔너리 [리스트] 꼴을 이용하면 쉽게 풀 수 잇더
    count = {}
# TC에서 str2 먼저 검사 => char 하나씩 빼와서 count에 있으면 +1, 없으면 char칸을 추가해준다
# for str2 in test_case ==> 숫자를 for문으로 돌릴 순 없다. 바로 for char로 들어가주면 된다.
    for char in str2:
        if char in count:
            count[char]+=1
        else:
            count[char]=1

    max_val = 0
    score = 0

## 아래 구문이 관건 겁나 헷갈린다
### 최대값 / 최소값 혹은 최대/최소 빈도수를 확인하거나 할 때는 누적보다는 걍 비교해서 갈아치워주기
### 딕셔너리 리스트 조건문 제어문 못하면 죽기!!!!!!!!!

# 1. str1에서 char1 글자를 하나씩 꺼내준다
# 2. char1 글자가 count에 있는지 확인하고 점수를 꺼내준다
# 3. 만약 엇? char1의 글자가 count에도 있는 글자다?? => score에 즉시추가
# 4. 마무리로 score이 max_val보다 크다면? 갈아치워준다!
# ***** score = count[char1] 이부분 다시 복숩하기

    for char1 in str1:
        if char1 in count:
            score = count[char1]
        if score > max_val:
            max_val = score

    print(f'#{test_case} {max_val}')
