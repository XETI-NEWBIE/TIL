import sys
sys.stdin = open("input.txt", "r")

passcode = {
        '0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9
}

test = int(input())

for test_case in range(1,test+1):
    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]

# 각 줄을 입력받아서 해당 줄에 1이 있는지 확인
# 1이 존재한다면 => 암호코드 스캔 위해 저장
# 코드가 존재하는 줄 단락 찾기
    target_row = -1
    for i in range(n):
        if '1' in arr[i]:
            target_row = i
            break

    # 예외 처리: 1이 있는 줄을 못 찾았다면 0 출력하고 다음 테스트 케이스로
    if target_row == -1:
        print(f'#{test_case} 0')
        continue

    line = arr[target_row]

# 암호코드의 끝점 찾기 위해
# 뒤에서부터 하나씩 확인 => 처음으로 0이 아닌 index 찾기
# => 암호코드의 끝 찾기 > 암호코드의 시작 찾기
    end_idx = -1
    for i in range(m-1,-1,-1):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        if line[i]=='1':
            end_idx = i
            break
    # 끝 - 시작 + 1 = 56
    # 시작 = 끝 - 56 + 1
    start_idx = end_idx - 56 + 1
    
    # 미리 만들어준 해독 dict를 이용해
    # 암호 코드를 7글자씩 잘라서 각 숫자를 해독
    password = []
    for i in range(start_idx, end_idx+1, 7):
        password.append(passcode.get(line[i:i+7]))

    odd_sum = password[0] + password[2] + password[4] + password[6]
    even_sum = password[1] + password[3] + password[5] + password[7]

    # (홀수합 * 3) + 짝수합 이 10의 배수인지 확인
    if (odd_sum * 3 + even_sum) % 10 == 0:
        # 올바른 암호면 숫자들의 총합 출력 
        print(f'#{test_case} {sum(password)}')
    else:
        # 잘못된 암호면 0 출력 
        print(f'#{test_case} 0')

