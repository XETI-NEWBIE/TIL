import sys
# sys.stdin = open("part_sum.txt", "r")

tests = int(input())
for test_case in range(1, tests+1):
    a_len, b_len = map(int, input().split())
    a_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))

    # 내가 지금 필요로 하는 B의 위치를 나타내는 변수 만들기
    target = 0

    # A 수열의 원소를 하나씩 살핀다
    for a_num in a_nums:
        # 만약 현재 보고있는 A의 원소가
        # 내가 필요로 하는 B의 원소라면
        if a_num == b_nums[target]:
            # 내가 확인할 B의 원소를 다음 원소로 지정한다.
            target += 1
    # (A를 다 살피거나) B를 다 찾을 때까지 반복한다.
    if target == b_len:
        break

    # 만약 target이 b_len과 동일하다면 YES
    # 보다 작다면 NO
    result = YES if target == b_len else 'No'