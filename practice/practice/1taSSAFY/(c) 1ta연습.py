
white_x = balls[0][0]
white_y = balls[0][1]

target_indices=[1,3,5]
target_idx = -1

for idx in target_indices:
    if balls[idx][0]!=-1:
        target_idx=idx
        break

target_x = balls[target_idx][0]
target_y = balls[target_idx][1]

best_hole=HOLES[0]
min_dist=9999
for hole in HOLES:
    dist = math.sqrt((hole[0]-target_x)**2 + (hole[1]-target_y)**2)
    if dist<min_dist:
        min_dist=dist
        best_hole=hole

angle_to_hole = math.atan2(best_hole[1]-target_y, best_hole[0]-target_x)
main_target_x = target_x-5.73*math.cos(angle_to_hole)
main_target_y = target_y-5.73*math.sin(angle_to_hole)

# # 1단계: 원래 하던 대로 '접점'을 먼저 구합니다. (홀의 반대 방향 5.73cm)
# angle_to_hole = math.atan2(best_hole[1] - target_y, best_hole[0] - target_x)
# contact_x = target_x - 5.73 * math.cos(angle_to_hole)
# contact_y = target_y - 5.73 * math.sin(angle_to_hole)

# # 2단계: 이 '접점'을 아래쪽 벽(y=0) 너머로 대칭 이동시킵니다.
# # 이게 바로 100점짜리 1쿠션의 목적지입니다.
# final_target_x = contact_x
# final_target_y = -contact_y

dx = main_target_x - white_x
dy = main_target_y - white_y

angle = math.degrees(math.atan2(dy,dx))

if angle<0:
    angle+=360

power = 100.0

print(f'{target_idx},{angle}, {power}')

########################################################################

white_x = balls[0][0]
white_y=balls[0][1]

target_indices = [1,3,5]
target_idx = -1

for idx in target_indices:
    if balls[idx][0]!=-1:
        target_idx=idx
        break

target_x = balls[target_idx][0]
target_y = balls[target_idx][1]

best_hole = HOLES[0]
min_dist = 9999
for hole in HOLES:
    #################### x좌표, y좌표 오타 틀림 !!!!!!!!#######################
    dist = math.sqrt((hole[0]-target_x)**2 + (hole[1]-target_y)**2)
    if dist<min_dist:
        min_dist = dist
        best_hole = hole

angle_to_hole = math.atan2(best_hole[1]-target_y, best_hole[0]-target_x)
main_target_x = target_x - 5.73*math.cos(angle_to_hole)
main_target_y = target_y - 5.73*math.sin(angle_to_hole)

#쿠션 로직
#angle_to_hole=math.atan2(best_hole[1]-target_y, best_hole[0]-target_x)
#contact_target_x = target_x - 5.73*math.cos(angle_to_hole)
#contact_target_y = target_y - 5.73*math.sin(angle_to_hole)
#main_target_x = contact_target_x
#main_target_y = contact_target_y

dx = main_target_x - white_x
dy = main_target_y - white_y

#################### atan2 (dx,dy 순서 틀림) !!!!!!!!#######################
angle = math.degrees(math.atan2(dy,dx))

if angle<0:
    angle+=360

power = 100.0

print({target_idx}, {angle}, {power})