############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.




def categorize_books(books):
    # [1단계] 탈출구 (Base Case)
    # 리스트가 비어있으면(더 이상 정리할 책이 없으면) 빈 딕셔너리를 반환하고 끝냅니다.
    
    if not books:
        return {}

    # [2단계] 떠넘기기 (Recursive Step)
    # 맨 앞의 책 한 권(books[0])은 내가 챙길 테니까, 
    # 나머지 책들(books[1:])은 함수 네가 다시 돌아서 정리해와! 라고 시킵니다.
    result_dictionary = categorize_books(books[1:])

    # [3단계] 내가 할 일 (Processing)
    # 함수가 남은 책들을 정리해서 가져온 수첩(result_dictionary)에 
    # 내가 맡은 첫 번째 책의 정보를 추가합니다.
    first_book = books[0]
    category = first_book['category']
    title = first_book['title']

    # 만약 수첩에 이 카테고리가 아직 없다면, 리스트를 새로 만들어줍니다.
    if category not in result_dictionary:
        result_dictionary[category] = []
    
    # 책 제목을 해당 카테고리 리스트에 넣습니다.
    # 재귀는 끝에서부터 돌아오기 때문에 insert(0, title)을 쓰면 문제 예시와 순서가 똑같아집니다.
    result_dictionary[category].insert(0, title)

    return result_dictionary


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

