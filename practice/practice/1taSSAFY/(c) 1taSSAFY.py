

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

# 일타싸피 Pass용 최종 통합 코드 (접점 + 1쿠션 선택형)
# === [1] 내 공과 타겟 공 위치 파악 ===
white_x = balls[0][0]
white_y = balls[0][1]

# === [1] 타겟 공 정하기 (채원님이 좋아하는 깔끔한 for문 버전) ===
target_indices = [1, 3, 5]
target_idx = -1

for idx in target_indices:
    if balls[idx][0] != -1: # 공이 살아있으면 (-1이 아니면)
        target_idx = idx
        break

target_x = balls[target_idx][0]
target_y = balls[target_idx][1]

# === [2] 타겟 공에서 가장 가까운 홀(Hole) 찾기 ===
best_hole = HOLES[0]
min_dist = 9999
for hole in HOLES:
# 1. (hole[0] - target_x): 구멍과 공의 '가로 거리' 차이를 구합니다.
# 2. (hole[1] - target_y): 구멍과 공의 '세로 거리' 차이를 구합니다.
# 3. ** 2: 각각의 차이를 '제곱'합니다. (음수가 나와도 양수로 만들기 위해 + 피타고라스 공식)
# 4. math.sqrt: 제곱해서 더한 값에 '루트'를 씌워 최종적인 '직선 거리'를 뽑아냅니다.
    dist = math.sqrt((hole[0] - target_x)**2 + (hole[1] - target_y)**2)
    if dist < min_dist:
        min_dist = dist
        best_hole = hole

# === [3] 목표 지점(final_target) 결정 ===
# 기본: 접점(Contact Point) 계산 (타겟 공 뒤 5.73cm 지점)
# 목적구가 hole을 향해 굴러가야할 방향 미리 계산해두는 것
# "홀까지 가려면 이 방향으로 굴러가야 해!"라는 내비게이션 정보
angle_to_hole = math.atan2(best_hole[1] - target_y, best_hole[0] - target_x)
# 2. 목적구 중심에서 홀 반대 방향으로 5.73cm 떨어진 '진짜 목표 지점(x)'을 구합니다.
# target_x(현재 위치)에서 가로로 이동할 양을 뺍니다.
# math.cos :각도 방향으로 1만큼 갈 때의 가로 길이 (옆으로 얼만큼 가냐)
final_target_x = target_x - 5.73 * math.cos(angle_to_hole)
# 3. 목적구 중심에서 홀 반대 방향으로 5.73cm 떨어진 '진짜 목표 지점(y)'을 구합니다.
# target_y(현재 위치)에서 세로로 이동할 양을 뺍니다.
# math.sin : 각도 방향으로 1만큼 갈 때의 세로 길이 (위로 얼만큼 가냐)
final_target_y = target_y - 5.73 * math.sin(angle_to_hole)

# # 1단계: 원래 하던 대로 '접점'을 먼저 구합니다. (홀의 반대 방향 5.73cm)
# angle_to_hole = math.atan2(best_hole[1] - target_y, best_hole[0] - target_x)
# contact_x = target_x - 5.73 * math.cos(angle_to_hole)
# contact_y = target_y - 5.73 * math.sin(angle_to_hole)

# # 2단계: 이 '접점'을 아래쪽 벽(y=0) 너머로 대칭 이동시킵니다.
# # 이게 바로 100점짜리 1쿠션의 목적지입니다.
# final_target_x = contact_x
# final_target_y = -contact_y

# === [4] 최종 각도 및 파워 계산 ===
# 내 흰 공에서 '최종 목표 지점'을 향해 조준 가이드]
dy = final_target_y - white_y
dx = final_target_x - white_x

# atan2로 각도 구하고 degrees로 변환 (음수면 +360)
angle = math.degrees(math.atan2(dy, dx))
if angle < 0: 
    angle += 360

# 파워는 채원님의 전략대로 무조건 풀파워 100 가이드]
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
