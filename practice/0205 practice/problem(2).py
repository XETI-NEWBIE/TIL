############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

'''
조건부 개수 세기 : 리스트 돌면서 특정조건 (길이 N 이상) 에 맞는 데이터만 골라낼 수 있는가?
** 길이 필터링
: 리스트에서 각 단어의 길이를 체크하는 if문 활용 능력

'''

def count_long_words(words, min_length):
    count = 0 # 조건에 맞는 단어 개수. 단어 몇 개 셌는지 기억시켜놓는 것.
    # list에서 단어 하나씩 꺼내보기
    for word in words:
        # 단어 길이 저장고 초기화
        word_length = 0
        # 단어에서 a,b,c...직접 한 글자씩 세어보기
        for char in word:
            # 한 단어 안에서 지금까지 몇 글자 셌는지 기억시켜놓기(counting) 
            word_length += 1
            
        # 직접 센 길이가 기준보다 크거나 같으면
        if word_length >= min_length:
            count += 1
            
    return count

# def count_long_words(words, min_length):
#     count=0
    
# for word in words:
#     word_length = 0
    
#     for char in word:
#         word_length += 1
    
#     if word_length>=min_length:
#         count+=1
        
#     return count


    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_long_words(['apple', 'banana', 'cat', 'dog'], 4))  # 2 ('apple', 'banana')
print(count_long_words(['a', 'bb', 'ccc'], 5))                 # 0
#####################################################


# def count_long_words(words, min_length):
#     word_length=0
#     count=0