


# 주현이 명강의 ~~~ 집가서 꼭 복습해보기

#import sys
#sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    T = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    for x in range(100):
        if ladder[99][x]==2:
            target = x
            break

    height = 99

    while height > 0:
        # if문 조건 만족할 경우 => while 반복 실행 ( 좌/우로 나눠서 gogo )
        if target > 0 and ladder[height][target-1]==1:
            while target > 0 and ladder[height][target-1]==1:
                target -= 1
            height-=1
        elif target<99 and ladder[height][target+1]==1:
            while target < 99 and ladder[height][target+1]==1:
                target += 1
            height-=1
        else:
            height-=1

    print(f'#{test_case} {target}')