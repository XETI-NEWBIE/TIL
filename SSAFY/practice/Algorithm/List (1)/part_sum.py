
import sys
# sys.stdin = open("part_sum.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 길이 정보 입력 (N= A길이, M= B길이)
    N, M = map(int, input().split())

    # 수열 A, B 리스트로 입력 받기
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    b_idx = 0 # B의 몇 번째 숫자를 찾고 있는지 가리키는 카운트 저장고

    for num in A: # A를 순서대로 탐색
        # 1. 아직 B를 다 못 찾았고 (b_idx < M)
        # 2. 현재 A의 숫자가 우리가 찾는 B의 숫자와 같다면?
        if b_idx < M and num == B[b_idx]:
            b_idx += 1 # 다음 타겟으로 이동 (카운트 증가)

    # B의 길이만큼 다 찾았으면 부분 수열임
    if b_idx == M:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")