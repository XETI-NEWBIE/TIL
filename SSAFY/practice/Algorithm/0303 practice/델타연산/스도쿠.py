T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1  # 일단 정답(1)이라고 믿고 시작!
    
    # 1. 가로, 세로 검사 (빈 리스트에 담기)
    for i in range(9):
        row_list = [] # 가로줄 숫자 담을 바구니
        col_list = [] # 세로줄 숫자 담을 바구니
        
        for j in range(9):
            row_list.append(arr[i][j])  # 가로줄 하나씩 쏙쏙
            col_list.append(arr[j][i])  # 세로줄 하나씩 쏙쏙
            
        # set()에 넣었을 때 길이가 9가 아니면? 중복된 숫자가 있다는 뜻!
        if len(set(row_list)) != 9 or len(set(col_list)) != 9:
            ans = 0
            break
            
    # 2. 3x3 격자 델타 검사
    if ans == 1: # 앞부분에서 안 틀렸을 때만 검사
        
        # 3x3 박스 9칸을 훑기 위한 델타값
        dr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        dc = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        
        # 박스의 시작점은 0, 3, 6 (징검다리처럼 뜀)
        for r in [0, 3, 6]:
            for c in [0, 3, 6]:
                box_list = [] # 박스 안 숫자 9개 담을 바구니
                
                # 시작점(r,c)에서 델타 방향으로 9칸 훑기
                for d in range(9):
                    ni = r + dr[d]
                    nj = c + dc[d]
                    box_list.append(arr[ni][nj])
                    
                # 9칸 다 담았는데 겹치는 게 있다면?
                if len(set(box_list)) != 9:
                    ans = 0
                    break

    print(f"#{tc} {ans}") #