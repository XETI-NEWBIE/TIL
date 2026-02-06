import sys

# sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):

    # 덤프 횟수 입력
    dump_limit = int(input())

    # 상자 높이 리스트 입력
    boxes = list(map(int, input().split()))

    # 덤프 수행
    for _ in range(dump_limit):
        # 가장 높은 곳과 낮은 곳의 인덱스를 찾음
        # (index 함수는 값이 여러 개여도 가장 앞의 인덱스를 반환하므로 안전함)
        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))

        # 평탄화 끝났으면(차이<=1) 반복 중단
        if boxes[max_idx] - boxes[min_idx] <= 1:
            break

        # 평탄화 작업 => 최고점 (-), 최저점 (+)
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    result = max(boxes) - min(boxes)

    print(f"#{test_case} {result}")