

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

# 1. 내 공(흰 공)의 좌표
white_x = balls[0][0]
white_y = balls[0][1]

# 1. 내가 노릴 후보 공들의 리스트를 만듭니다.
# balls[1]은 1번 공, balls[3]은 3번 공, balls[5]는 8번 공의 좌표입니다.
target_indices = [1, 3, 5]
target_idx = -1 # 아직 누굴 칠지 못 정했다는 뜻의 초기값

# 2. 후보들을 하나씩 찔러봅니다 (반복문)
for idx in target_indices:
    # balls[idx][0]은 그 공의 x좌표입니다.
    # 이게 -1이 아니라는 건, 아직 구멍에 안 들어갔다는 뜻입니다!
    if balls[idx][0] != -1:
        target_idx = idx # "찾았다! 이번에 내가 칠 놈은 너다!"
        break            # 타겟을 찾았으니 뒤에 남은 후보는 더 볼 필요 없이 반복문을 끝냅니다.

# === [3] 결정된 타겟의 좌표를 변수에 저장 ===
# 타겟 공의 번호(target_idx)를 알았으니, 이제 그 공의 실제 X, Y 좌표를 가져옵니다.]
# balls[target_idx]는 [x좌표, y좌표] 형태의 리스트입니다.]
target_x = balls[target_idx][0]  # 타겟 공의 가로 위치 (X)
target_y = balls[target_idx][1]  # 타겟 공의 세로 위치 (Y)

# === [4] 내 공에서 타겟 공까지의 거리 차이 구하기 ===
# 각도를 구하기 위해 내 공과 타겟 공 사이의 가로(dx), 세로(dy) 거리를 구합니다. 가이드]
# 공식: "목표 지점 - 내 위치" (순서가 바뀌면 정반대로 쏘게 되니 주의하세요!) 가이드]
dy = target_y - white_y  # 세로 방향으로 얼마만큼 떨어져 있나? (높이)
dx = target_x - white_x  # 가로 방향으로 얼마만큼 떨어져 있나? (밑변)

# === [5] 삼각함수를 이용한 샷 각도 계산 ===
# math.atan2(y, x)는 밑변과 높이의 길이를 받아 사분면을 고려한 정확한 각도를 라디안으로 반환합니다. 가이드]
# atan()과 달리 x가 0일 때의 에러(ZeroDivisionError)도 알아서 처리해 주는 똑똑한 함수입니다. 가이드]
angle_white_to_target = math.atan2(dy, dx) 

# 라디안(Radian) 단위를 우리가 아는 도(Degree, 0~360도) 단위로 변환합니다. 가이드]
# 변환 공식: 도 = 라디안 * (180 / pi)]
angle = math.degrees(angle_white_to_target)

# === [6] 음수 각도 보정 (Safety Net) ===
# math.atan2는 -180도에서 +180도 사이의 값을 반환합니다. 가이드]
# 게임 서버가 양수 각도만 이해할 수 있으므로, 음수가 나오면 한 바퀴(360도)를 더해 보정합니다. 가이드]
# 예: -90도(아래쪽) + 360도 = 270도 (똑같이 아래쪽을 의미함)
if angle < 0:
    angle += 360

# === [7] 샷 파워 설정 (The Full Send) ===
# 힘 조절을 하다가 목적구까지 공이 도달하지 못하면 파울(공을 아무것도 맞히지 못함)이 됩니다.
# 확실하게 목적구를 맞히기 위해 서버 허용 최대치인 100으로 설정합니다., image_10e3c6.jpg]
power = 100.0

# === [8] 최종 결과 확인용 출력 ===
# 계산이 잘 되었는지 확인하기 위해 화면에 출력합니다. (실제 서버 전송 데이터는 아닙니다.)]
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
