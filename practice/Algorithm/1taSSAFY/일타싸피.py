
import math

# 기준점과 목표 지점 좌표 정의하기
my_ball=(1,1)
target=(2,2)

# 1. 두 점 사이의 거리 계산 (피타고라스 정리)
# x 좌표의 차이와 y 차이의 차이를 각각 제곱하여 더한 후 제곱근 구하기
delta_x=target[0]-my_ball[0]
delta_y=target[1]-my_ball[1]
distance=math.sqrt(delta_x**2+delta_y**2)

# 2. 두 점 사이의 각도 계산 (atan 함수 활용)
# atan 함수는 기울기(y변화량/x변화량)를 인자로 받아 각도를 리디안으로 변환
# x 좌표의 차이가 0일 경우 => zerodivisionerror가 발생할 수 있음
# if delta_x==0:
#     # x에 변화가 없을 때 (수직선), 각도는 90도
#     angle_radians=math.pi/2
# # 기울기 : slope
# # rad 각도 : angle_radians
# else:
#     slope=delta_y/delta_x
#     angle_radians=math.atan(slope)

angle_radians=math.atan2(delta_x, delta_y)

# radian 단위를 도(degree)단위로 변환
angle_degrees=math.degrees(angle_radians)

# 결과 출력
print(f'거리:{distance:.2f}, 각도:{angle_degrees}°')

##########################################################################

import math
# 기준점 (A)의 좌표를 (0,0)으로 설정
mine_x, mine_y = 0,0
# 목표 지점들의 좌표 리스트
target_point=[[1,2],(-2,-3),(3,1),(-1,4)]
point_info_list=[]

# 모든 목표 지점을 순회하며 정보 계산
for point_x, point_y in target_point:
    # 1. 거리 계산 (피타고라스의 정리)
    distance_from_me=math.sqrt(
        (point_x - mine_x)**2+(point_x - mine_y)**2
    )

# 2. 각도 계산하기 (atan2 함수로 바로 해결)
# atan2(y,x) 순서로 인자를 전달 => 정확한 각도 (rad) 계산
angle_radians=math.atan2(point_y-mine_y, point_x-mine_x)
# radian 단위를 degree 단위로 변환
angle_degrees = math.degrees(angle_radians)

# 3. 계산된 정보를 리스트에 추가
# 데이터 구조를 튜플로 명시적 표현
point_data=(distance_from_me, angle_degrees, (point_x, point_y))
point_info_list.append(point_data)

# 4. 거리순으로 정렬
# 리스트의 각 튜플은 첫번째 요소(거리)를 기준으로 자동 정렬
point_info_list.sort()

# 5. 두 번째로 가까운 점의 정보 선택
second_closest_point=point_info_list[1]

# 6. 결과 출력
distance = second_closest_point[0]
angle = second_closest_point[1]
point_coords=second_closest_point[2]

print(f'점의 위치 : {point_coords}, 거리 : {distance:.2f}, 각도 : {angle:.2f}°')