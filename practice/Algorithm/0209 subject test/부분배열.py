

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

'''
1. 반복문 범위 문법 오류 (range)

작성: for test_case in (1, T + 1): -> 이것은 1과 T+1 두 개의 숫자만 튜플로 도는 것입니다.

수정: for test_case in range(1, T + 1):로 바꿔야 1부터 T까지 반복합니다.

2. 입력 처리 방식 (input)

작성: map(input().split()) -> map은 함수가 필요한데 인자가 빠졌고, 예시 입력은 공백 없는 문자열입니다.

수정: 그냥 A = input(), B = input()으로 문자열 자체를 받는 것이 깔끔합니다.

3. 자료형 및 메소드 오류 (pop)

작성: reversed_B.pop() -> reversed_B는 문자열(str)인데, 파이썬 문자열은 변경 불가능(immutable)하며 pop() 메소드가 없습니다.

4. 로직 및 출력 요구사항 불일치

작성: 단어를 모아서(collect_bag) 출력하려 함.

수정: 문제의 요구사항은 단어를 완성했을 때 마지막으로 가져온 카드의 <<<인덱스 번호>>>를 출력하는 것입니다.

'''

# 수정 코드 --- greedy 방식

T = int(input())

for test_case in range(1, T + 1):
    # N: 벨트 길이, M: 타겟 단어 길이
    N, M = map(int, input().split())
    
    # A: 컨베이어 벨트 문자열, B: 만들어야 할 단어
    A = input().strip()
    B = input().strip()
    
    target_idx = 0  # 우리가 B에서 찾아야 할 글자의 인덱스
    result_idx = -1 # 결과값 (못 찾으면 -1)

    # 벨트 A를 처음부터 끝까지 한 번만 훑습니다 (순서대로니까요)
    for i in range(N):
        # 벨트의 글자(A[i])가 우리가 찾는 단어의 현재 글자(B[target_idx])와 같다면?
        if A[i] == B[target_idx]:
            target_idx += 1 # 다음 글자를 찾으러 갑니다
            
            # B의 모든 글자를 다 찾았다면?
            if target_idx == M:
                result_idx = i # 현재 벨트의 위치(i)가 정답
                break # 탐색 종료

    print(f'#{test_case} {result_idx}')


"""
초기값 (result_idx = -1) : "아직 못 찾았음"

처음에는 탐정이 조사를 시작하기도 전입니다. 

그래서 "못 찾았다"는 뜻의 기본값 -1을 미리 적어두는 것입니다. 

만약 루프가 다 돌 때까지 단어를 완성하지 못하면, 이 -1이 그대로 보고서에 남게 됩니다.

루프 안에서의 변화 (result_idx = i) : "드디어 찾았다!"

벨트의 i번째 칸을 지나가며 검사를 합니다. 


if target_idx == M: 이 조건이 참이 되는 순간은 **"단어의 마지막 글자까지 다 찾은 순간"**입니다. 

그때 탐정은 보고서에 적혀있던 -1을 싹 지우고, **"지금 서 있는 위치인 i번 칸"**으로 다시 적습니다. 

중단 (break) : "이제 퇴근!"

정답을 찾았으니 더 이상 벨트 뒤쪽을 볼 필요가 없습니다. break를 통해 반복문을 즉시 빠져나옵니다. 

출력 (print) : "보고서 제출"

루프 밖으로 나와서 최종적으로 적혀 있는 result_idx 값을 보여줍니다.
"""


# 수정 코드 (gemini) --- pop() 사용

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    # 벨트(A)는 그대로 문자열로 둡니다.
    A = input().strip()
    # 찾아야 할 단어(B)는 하나씩 지우기 위해 '리스트'로 만듭니다.
    # 예: "SSAFY" -> ['S', 'S', 'A', 'F', 'Y']
    target_list = list(input().strip()) 
    
    result = -1 # 못 찾았을 때 기본값 설정

    # 벨트 위를 0번부터 N-1번까지 지나갑니다 (i는 벨트 위의 현재 위치 인덱스)
    # i는 자동으로 0부터 N-1 까지의 숫자가 된다
    for i in range(N):
        # 1. 아직 찾을 단어가 남아있는가?
        # 2. 벨트의 현재 글자(A[i])가 찾아야 할 단어의 '맨 앞 글자'와 같다면?
        # target의 길이가 0 이상이고 A의 i번째 idx가 target의 첫 글자와 같다면
        if len(target_list) > 0 and A[i] == target_list[0]:
            target_list.pop(0) # 찾았으니 리스트 맨 앞을 지워버립니다!
            
            # 리스트가 텅 비었다면 다 찾은 것!
            if len(target_list) == 0:
                result = i # 현재 위치(i)가 정답
                break # 더 볼 필요 없이 종료

    print(f'#{test_case} {result}')


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

