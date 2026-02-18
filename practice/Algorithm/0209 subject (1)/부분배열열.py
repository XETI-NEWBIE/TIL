

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
    
    target = 0  # 우리가 B에서 찾아야 할 글자의 인덱스
    result = -1 # 결과값 (못 찾으면 -1)

    # 벨트 A를 처음부터 끝까지 한 번만 훑습니다 (순서대로니까요)
    for i in range(N):
        # 벨트의 글자(A[i])가 우리가 찾는 단어의 현재 글자(B[target_idx])와 같다면?
        # target: "내가 지금 B에서 찾아야 할 글자의 순서" 
        # A[i] : "문자열 A에서 i번째 위치에 있는 글자를 가져와라"라는 뜻
        if A[i] == B[target]:
            target += 1 # 다음 글자를 찾으러 갑니다
            
            # B의 모든 글자를 다 찾았다면?
            if target == M:
                result = i # 현재 벨트의 위치(i)가 정답
                break # 탐색 종료

    print(f'#{test_case} {result}')


"""
Q. A[i] == B[target]은 무슨 원리인가요?
이 부분은 **"내가 지금 벨트에서 보고 있는 글자가, 내가 만들어야 할 단어의 '몇 번째' 글자인가?"**를 체크하는 곳입니다.

A (벨트): S S F A S F F S Y S

B (목표 단어): S S A F Y

target: "내가 지금 B에서 찾아야 할 글자의 순서" (처음엔 0번인 S를 찾아야 하죠)

진행 과정을 상상해 보세요:

i = 0일 때)  A[0]은 'S'입니다. B[target]도 'S'죠? (일치!)

target을 1로 올립니다. "이제 다음 글자인 B[1]('S')을 찾을 차례야!"라고 표시하는 거죠.

i = 1일 때) A[1]은 'S'입니다. B[1]도 'S'죠? (일치!)

target을 2로 올립니다. "자, 이제 세 번째 글자 B[2]('A')를 찾자!"

i = 2일 때) A[2]는 'F'입니다. 근데 우리는 지금 'A'를 찾아야 해요. (불일치)

그냥 지나갑니다. target은 그대로 2입니다.

이렇게 target은 **"다음에 내가 낚아채야 할 단어의 위치"**를 가리키는 화살표라고 생각하시면 됩니다.
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

