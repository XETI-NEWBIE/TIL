

# python_code_adv.py

import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'Player1'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    ###############################
    # 공 번호 i ㅡ 0(흰공), 1(1), ..., 4(4), 5(8번)
    # 공 위치 x = balls[i][0]
    # 공 위치 y = balls[i][1]
    # Data Received: 64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/ ㅡ> (64,64),(250,122),(-1,-1),(-1,-1),(-1,-1),(-1,-1)


# 내 공 좌표
white_x=balls[0][0]
white_y=balls[0][1]

# 목적구의 빈 리스트 생성
# 5번은 8번공을 의미함
target_indices=[1,3,5]
target_idx=-1

# 목적구 공들 돌아갈 로직짜기
for idx in target_indices:
    if balls[idx][0]!=-1:
        target_idx=idx
        break

'''
***** 이거완전미친넘아녀 balls인덱스를 불러와야지 
냅다 대괄호에 숫자만 꼬라박고 있네!!!!!!!!!뭐하냐!!!!!!!!*******

white_x = balls[0][0]
white_y = balls[0][1]

target_indices=[1,3,5]
target_idx=-1

*********** 미친놈아!!!! balls[target_idx]가 아니라
balls[idx]지 target_idx를 여기에 왜 불러오냐!!!!!!!!!*************
그리고 break도 안에다 넣어줘야지 뭐하냐

for idx in target_indices:
    if balls[idx][0]!=-1:
        target_idx=idx
        break

target_x = balls[target_idx][0]
target_y = balls[target_idx][1]

dx = target_x - white_x
dy = target_y - white_y

origin_angle = math.atan2(dy,dx)
angle = math.degrees(origin_angle)

if angle<0:
    angle+=360

power = 100.0

print(f'{target_idx}, {angle}, {power})
'''

# 결정된 타겟들의 좌표를 변수에 저장
# balls 라는 큰 리스트의 이번 turn 목적구의 [0]:x좌표, [1]:y좌표
target_x = balls[target_idx][0]
target_y = balls[target_idx][1]

# 거리 차이 구해줘야지
dx = target_x - white_x
dy = target_y - white_y

# atan2를 통해 삼각함수를 이용한 샷 각도 계산
# origin_angle = math.atan2(dy,dx)

# # radian=>degree로 변환
# angle = math.degrees(origin_angle)

angle = math.degrees(math.atan2(dy, dx))

# 음수 각도 보정
if angle<0:
    angle+=360

# 힘 세기 설정
power=100.0

print(f'{target_idx}, {angle:.2f}, {power:.2f}')