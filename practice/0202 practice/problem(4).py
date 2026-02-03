############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 기능: collections.Counter, List.count
# 기본 점수 (9점): 제한 내장 기능을 사용한 해결
# 가산점(+3점): 제한 내장 기능없이 직접 구현 (총 12점)
'''
빈도수 측정 (counting)
: 데이터를 딕셔너리에 담아 각 항목이 몇 개씩 나왔는지 기록할 수 있는가?

딕셔너리 (key-value)를 생성하고 관리하는 방법을 아는지 확인하려는 의도
'''
def count_menus(orders):
    menu_count = {}  # 메뉴 개수를 적을 빈 수첩(딕셔너리)

    for menu in orders:
        # 수첩에 이미 적힌 메뉴라면?
        if menu in menu_count:
            menu_count[menu] += 1  # 개수 1개 추가
        # 처음 보는 메뉴라면?
        else:
            menu_count[menu] = 1   # 개수 1개로 시작
            
    return menu_count
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_menus(['Ice Americano', 'Latte', 'Ice Americano', 'Mocha', 'Latte']))
# {'Ice Americano': 2, 'Latte': 2, 'Mocha': 1} (순서는 무관)
print(count_menus(['Cocoa', 'Cocoa', 'Cocoa'])) # {'Cocoa': 3}
#####################################################