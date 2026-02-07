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
    menu_note = {}  # 메뉴 개수를 적을 빈 수첩(딕셔너리)
    #  (메뉴) (입력받은 데이터 뭉치)
    for menu in orders:
        # if menu in menu_note => 빈 메뉴 수첩에 메뉴가 있는지 없는지 여부를 판단
        if menu in menu_note:
            menu_note[menu] += 1  # 개수 1개 추가
        # 처음 보는 메뉴라면?
        # 아예 빈 수첩에 메뉴 칸 새로 만들어버리기 ㅋㅋ 
        else:
            menu_note[menu] = 1   # 개수 1개로 시작
            
    return menu_note

# menu_note[menu] => 빈 수첩에서 americano / latte라고 써진 칸을 의미


def count_menus(orders):
    menu_note = {}
    
    for menu in orders:
        if menu in menu_note:
            menu_note[menu] += 1
        else:
            menu_note[menu]=1
            
    return menu_note








  
######################################################################

def count_menus(orders):
    menu_note = {}
    
    for menu in orders:
        # .get(menu, 0)의 뜻: 
        # "수첩에서 menu 찾아봐. 없으면 일단 0이라고 쳐!"
        # 거기다가 1을 더해서 다시 저장해!
        menu_note[menu] = menu_note.get(menu, 0)+1 # 이 때 1은 몇 개 가져왔는지! 가져온 횟수라고 할 수 있음 
        # 빈 수첩의 menu 칸에다가 get을 활용해서 menu 값을 key값으로, 기본값을 0으로 두고 counting +1
        # .get 메서드 =
        
    return menu_note

# dict[list] 형태에선 dict['latte']나 dict['Americano'] 같은 경우를 봤을 때 list 안의 이름이 곧 KEY 값이 된다.
# .get 메서드가 가져올 수 있는건 사실상 key값뿐 => menu_note[menu]에다 get값을 할당한다고 한다면 menu가 곧 키값이 된다. 


#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(count_menus(['Ice Americano', 'Latte', 'Ice Americano', 'Mocha', 'Latte']))
# {'Ice Americano': 2, 'Latte': 2, 'Mocha': 1} (순서는 무관)
print(count_menus(['Cocoa', 'Cocoa', 'Cocoa'])) # {'Cocoa': 3}
#####################################################




# def count_menus(orders):
#     menu_note = {}
#     # set(orders)를 하면 중복이 제거된 메뉴 이름만 남음
#     # 예: ['Latte', 'Mocha', 'Latte'] -> {'Latte', 'Mocha'}
#     unique_menus = set(orders)
    
#     for menu in unique_menus:
#         # 메뉴판에 있는 메뉴를 하나씩 꺼내서
#         count = 0
#         for order in orders:
#             if order == menu:
#                 count += 1
#         # 다 셌으면 수첩에 기록!
#         menu_note[menu] = count
        
#     return menu_note