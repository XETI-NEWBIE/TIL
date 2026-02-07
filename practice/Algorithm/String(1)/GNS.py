
# 버블 소트와 카운팅 소트, 셀렉션 소트 알아두기 !!!

import sys
sys.stdin = open("GNS_test_input.txt", "r")

# T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
    # ZRO = 0
    # ONE = 1
    # TWO = 2
    # THR = 3
    # FOR = 4
    # FIV = 5
    # SIX = 6
    # SVN = 7
    # EGT = 8
    # NIN = 9
    # # input.split()만 해줘도 이미 문자열 출력 OK임
    # num = input().split()
    # num_list = sorted(num)
    # print(f'#{test_case}{num_list}')

'''
tc = input().split()
for tc in range(1,10+1):
    tc += 1

    tc_length = input().split()
    alien_num = input().split()

    num_list = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    alien_list = dict(sorted(alien_num.items(num_list)))
       ======> list와 items 등 아는게 없으니 구글링 빠르게 해보고 개념익히고 적용해보는 방식으로 연습하기

    print(f'#{tc} {alien_num}')
'''

# 입력값에 이미 번호가 있으므로 또 따로 입력해줄 필요 x. for _ 로 처리한다
# 절차를 먼저 작성하고, 절차에 맞는 코드 작성하기

'''

# 반드시 내가 뭘 하고 싶은지 주석으로 쓰고 바로 아래에 코드 쓰는 식으로 전개하기
# 내가 뭘 하고싶은지 씀으로써 그 다음의 코드를 쓸 수 있고 작성할 수 있다

'''

T = int(input())

for _ in range(T):
    # 이 문제처럼 문자열의 길이가 제거된 형태로 출력하려면 input().split()에 변수 하나가 아닌 두 개를 때려주면 된다
    n, m = input().split()
    alien_nums = input().split()
    # num_list 에 하드코딩처럼 그냥 딕셔너리에 외계인 넘버를 지정해준다
    num_list = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    # lambda 로 해결 ! 딕셔너리의 key값만 가져와서 0부터 sort()로 정렬해준다
    alien_nums.sort(key=lambda x: num_list[x])
    # if) sorted를 썼다면?
    # sorted_list = sorted(alien_nums, key=lambda x: num_list[x])
    # print(n, *sorted_list, sep=" ")
    print(n, *alien_nums, sep=" ")










