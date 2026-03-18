# import sys
# # sys.stdin = open("part_sum.txt", "r")
#
# num = 456789 # baby gin을 확인할 6자리 수
# c = [0] * 12 # 6자리 수로부터 각 자리수 추출 => 개수 누적할 리스트 생성
#
# for change in str():
#
# i = 0
# tri = run = 0
#
# # 숫자=> str로 바꿔서 꺼냄
# for string in str(num):
#     c[int(string)] += 1 # 꺼낸 글자를 다시 숫자로 바꿔서 인덱스로 사용
#
# while i < 10:
#     # Tri & Run 검사 => continue : if 조건이 맞으면 i증가 X + 제자리에서 다시 검사 => 남은 카드로 그자리에서 또 만들 수 있으니 skip ㄴㄴ
#     # Triplet 조건 검사: 현재 숫자가 3개 이상 있으면?
#     if c[i] >= 3:
#         c[i] -= 3  # 3개를 덜어냄
#         tri += 1   # Tri 횟수 +1 증가
#         continue   # 또 Tri가 있을 수 있으니 i를 증가시키지 않고 다시 순회
#
#     # Run 검사: 현재 숫자부터 연속된 3개가 각각 1개 이상 있으면?
#     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
#         c[i] -= 1    # 하나씩 덜어냄
#         c[i+1] -= 1
#         c[i+2] -= 1
#         run += 1     # Run 성공 횟수 증가
#         continue     # 또 Run이 있을 수 있으니 다시 검사
#
#     # Tri도 Run도 아니면 다음 숫자로 넘어감
#         i += 1
#
# if tri + run == 2:
#     print("Baby Gin")
# else:
#     print("Lose")