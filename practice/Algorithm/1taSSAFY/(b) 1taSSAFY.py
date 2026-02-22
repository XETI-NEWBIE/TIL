

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

# 1. 내 공(흰 공) 위치
white_x, white_y = balls[0][0], balls[0][1]

# 2. 타겟 정하기 (1번 없으면 3번, 3번 없으면 8번)
target_idx = 1
if balls[1][0] == -1: target_idx = 3
if balls[1][0] == -1 and balls[3][0] == -1: target_idx = 5

target_x, target_y = balls[target_idx][0], balls[target_idx][1]

# 3. 가장 가까운 홀(Hole) 찾기
best_hole = HOLES[0]
min_dist = 9999
for hole in HOLES:
    dist = math.sqrt((hole[0] - target_x)**2 + (hole[1] - target_y)**2)
    if dist < min_dist:
        min_dist = dist
        best_hole = hole

# 4. 접점(Contact Point) 구하기 - 이 코드의 핵심!
# 타겟 공 중심에서 홀의 반대 방향으로 공의 직경(5.73)만큼 떨어진 점
angle_to_hole = math.atan2(best_hole[1] - target_y, best_hole[0] - target_x)
contact_x = target_x - 5.73 * math.cos(angle_to_hole)
contact_y = target_y - 5.73 * math.sin(angle_to_hole)

# 5. 흰 공에서 접점을 향해 치는 최종 각도 구하기
angle = math.degrees(math.atan2(contact_y - white_y, contact_x - white_x))
if angle < 0: 
    angle += 360

# 6. 파워는 무조건 개쎄게!
power = 100.0

print(f'Target: {target_idx}번 공, Angle: {angle:.2f}, Power: {power}')


# 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
# 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
#   - angle: 흰 공을 때려서 보낼 방향(각도)
#   - power: 흰 공을 때릴 힘의 세기
#
# 이 때 주의할 점은 power는 100을 초과할 수 없으며,
# power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
#
# 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
##############################

merged_data = '%f/%f/' % (angle, power)
sock.send(merged_data.encode('utf-8'))
print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
