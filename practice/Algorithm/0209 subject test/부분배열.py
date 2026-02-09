

T = int(input())
for test_case in (1, T + 1):
    # 벨트의 길이 N, 단어의 길이 M
    N, M = map(int, input().split())
    # A = N개의 글자카드, B = 스타티가 만들려는 단어
    A = list(map(input().split()))
    B = list(map(input().split()))
    # collect_bag에 카운트를 저장해준다
    collect_bag = []
    # B를 뒤집어준 뒤, pop메서드를 활용한다
    reversed_B = "".join(reversed(B))
    # A를 돌면서 탐색
    for word in A:
        # reversed_B 가 존재하고 word가 reversed_B의 마지막 글자와 일치 한다면?
        if reversed_B and word == reversed_B[-1]:
            # collect_bag에 reversed_B에서 .pop()을 통해 삭제한 값을 추가해준다
            collect_bag.append(reversed_B.pop())
        # collect_bag에 word와 일치한 reversed_B 배열이 담길 것이고, 해당 reversed_B 문자열의 최대 인덱스를 A에서 찾는다

    if not reversed_B and len(collect_bag) == M:
        print(f'#{test_case}', *collect_bag)
    else:
        print(f'#{test_case}', '-1')




# T = int(input())
# for test_case in (1, T + 1):
#     # 벨트의 길이 N, 단어의 길이 M
#     N, M = map(int, input().split())
#     # A = N개의 글자카드, B = 스타티가 만들려는 단어
#     # A = list(map(list, input().split("")))
#     A = input()
#     # B = list(map(input().split("")))
#     B = input()
#     # collect_bag에 카운트를 저장해준다
#     collect_bag = []
#     # B를 뒤집어준 뒤, pop메서드를 활용한다
#     reversed_B = "".join(reversed(B))
#     # A를 돌면서 탐색
#     for word in A:
#         # reversed_B 가 존재하고 word가 reversed_B의 마지막 글자와 일치 한다면?
#         if len(reversed_B) != 0 and word == reversed_B[-1]:
#             # collect_bag에 reversed_B에서 .pop()을 통해 삭제한 값을 추가해준다
#             collect_bag.append(reversed_B.pop())
#         # collect_bag에 word와 일치한 reversed_B 배열이 담길 것이고, 해당 reversed_B 문자열의 최대 인덱스를 A에서 찾는다0

#     if not reversed_B and len(collect_bag) == M:
#         print(f'#{test_case}', *collect_bag)
#     else:
#         print(f'#{test_case}', '-1')


# # 부분집합 판별
# T = int(input())
# for test_case in (1, T+1):
#     # 벨트의 길이 N, 단어의 길이 M
#     N, M = int(input())
#     # A = N개의 글자카드, B = 스타티가 만들려는 단어
#     A = list(map(input().split()))
#     B = list(map(input().split()))
#
#     collect_bag = []
#     # B를 뒤집어주기
#     reversed_B = "".join(reversed_B(B))
#
#     for word in A:
#         if B and word == B[-1]:
#             collect_bag.append(reversed_B.pop())
#         else:
#             break
#     if not reversed_B and len(collect_bag) == B:
#         print(f'#{test_case}  {collect_bag}')

