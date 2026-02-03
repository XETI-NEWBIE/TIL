############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def categorize_books(books):
    result = {} # 결과를 담을 빈 딕셔너리

    for book in books:
        category = book['category'] # 책의 분류(장르)
        title = book['title']       # 책 제목
        
        # 이 분류가 결과 딕셔너리에 없다면?
        if category not in result:
            result[category] = []   # 리스트를 새로 만들어줌
            
        # 해당 분류 리스트에 책 제목 추가
        result[category].append(title)
        
    return result
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
books_data = [
    {'title': 'Python Basic', 'category': 'IT'},
    {'title': 'Java Standard', 'category': 'IT'},
    {'title': 'History of World', 'category': 'History'},
    {'title': 'Cooking 101', 'category': 'Life'}
]
# 결과:
# {
#   'IT': ['Python Basic', 'Java Standard'],
#   'History': ['History of World'],
#   'Life': ['Cooking 101']
# }
print(categorize_books(books_data))
#####################################################