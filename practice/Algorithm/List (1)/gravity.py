
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    boxes = list(map(int, input().split()))

    # 최대 낙차를 기록할 변수
    max_fall = 0
    # 각 칸에 상자가 쌓인 높이를 확인한다.
    for i in range(n):
    # 나보다 높게 쌓인 (오른쪽) 상자들의 갯수를 기록할 변수를 만들고
        higher_boxes = 0

        # 나보다 오른쪽 상자들을 살펴본다.
        for j in range(i+1, n):
            # 만약 나보다 높거나 같으면
            if boxes[j] >= boxes[i]:
            #더 컸던 상자들의 갯수를 기록한다.
            higher_boxes += 1


    # 내가 낙하할 수 있는 최대 거리는
    # 내가 오른쪽에서 떨어진만큼 - 나를 방해하는 상자의 개수
     current_fall = (n-i-1) - higher_boxes
    # 나의 최대거리랑 기록된 최대 거리를 비교한다.
    if max_fall < current_fall:
        max_fall = current_fall

    print(f'#{test_case}{max_fall}')












