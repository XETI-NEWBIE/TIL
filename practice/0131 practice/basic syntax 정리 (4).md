'''
0131 practice.basic syntax 정리 (4)의 Docstring

fruit_list = input().split()
print(fruit_list)

# 예시 입력: 사과 바나나 체리

# 출력: ['사과', '바나나', '체리']

=>input.split 함수는 사용자가 입력한 문자열을 공백을 기준으로 나누어 리스트를 반환한다

- 메서드란?
  : 특정 자료형이 자신만의 기능을 위해 갖고 있는 특별한 함수
  자료형의 이름 뒤에 (.)을 찍고 메서드 이름을 이어 붙인다.
  ex) 리스트이름.append(요소), 리스트이름.insert(위치, 요소)

[ List method 종류 정리 ]

1. append() 메서드는 리스트의 끝에 새로운 요소를 추가한다

fruits = ["사과", "바나나", "체리"]
fruits.append("오렌지")
print(fruits) # 출력: ['사과', '바나나', '체리', '오렌지']

2. insert() 메서드는 지정한 인덱스 위치에 요소를 삽입한다.

fruits = ["사과", "바나나", "체리", "오렌지"]
fruits.insert(1, "키위")
print(fruits) # 출력: ['사과', '키위', '바나나', '체리', '오렌지']

3. remove() 메서드는 리스트에서 첫 번째로 일치하는 요소를 제거한다

fruits = ["사과", "키위", "바나나", "체리", "오렌지"]
fruits.remove("바나나")
print(fruits) # 출력: ['사과', '키위', '체리', '오렌지']

4. pop() 메서드는 지정한 인덱스의 요소를 제거하고 반환한다. 인덱스를 지정하지 않으면 마지막 요소가 제거

fruits = ["사과", "키위", "체리", "오렌지"]
last_fruit = fruits.pop()
print(last_fruit) # 출력: 오렌지
print(fruits) # 출력: ['사과', '키위', '체리']

second_fruit = fruits.pop(1)
print(second_fruit) # 출력: 키위
print(fruits) # 출력: ['사과', '체리']

5. sort() 메서드는 리스트를 오름차순으로 정렬한다

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers) # 출력: [1, 2, 5, 5, 6, 9]

- reverse = True 인자를 사용하여 내림차순으로 정렬할 수 있다.

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)
print(numbers) # 출력: [9, 6, 5, 5, 2, 1]

6. reverse() 메서드는 리스트의 요소 순서를 반대로 뒤집는다.

fruits = ["사과", "바나나", "체리"]
fruits.reverse()
print(fruits) # 출력: ['체리', '바나나', '사과']

7. count() 메서드는 리스트 내에서 특정 요소가 몇 번 등장하는지 반환한다.

numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2)) # 출력: 3

8. index() 메서드는 리스트 내에서 특정 요소가 처음으로 등장하는 위치의 인덱스를 반환한다.

fruits = ["사과", "바나나", "체리", "바나나"]
print(fruits.index("바나나")) # 출력: 1

- 특정 요소가 중복으로 등장할 경우, 첫번째 인덱스만 반환한다.

numbers = [10, 20, 30, 20, 40]
print(numbers.index(20)) # 출력: 1

9. len() 함수는 리스트에 포함된 요소의 개수(리스트의 길이)를 반환한다.
   len() 은 메서드가 아닌 함수이므로, tuple 이나 dict같은 다른 자료형에도 적용할 수 있다.

fruits = ["사과", "체리"]
print(len(fruits)) # 출력: 2

'''

리스트를 다룰 때 for문은 매우 자주 사용된다.
각 요소를 순서대로 꺼내와서 특정 연산 수행 or 조건에 따라 새로운 리스트 생성 가능

1. 인덱스를 사용하는 for문 (for i in range(len(list)))
   : 인덱스를 활용하면 리스트의 요소뿐만 아니라 해당 요소의 위치(index)에도 접근할 수 있다.
   이는 요소의 '위치'가 필요한 경우 유용하다.

-기본구조
for i in range(len(리스트)):
실행할 코드

- ex) 리스트 요소에 2배씩 곱하기 (index 활용)

original = [3, 1, 4, 1, 5]
doubled = []

for i in range(len(original)):
doubled.append(original[i] \* 2)

print(doubled)

# 출력: [6, 2, 8, 2, 10]

=> 위 예제에서는 range(len(original))을 사용하여 리스트의 index를 순회한다. 각 index를 통해 해당 요소에 접근하고, 두 배 한 값을 새로운 리스트 doubled에 추가한다.

2. 요소를 직접 순회하는 for문(for 변수 in 리스트)
   : 더 간결하고 가독성이 좋다. 리스트의 각 요소를 직접 순회 가능. index가 필요없는 경우 적합함.

- 기본구조

for 변수 in 리스트:
실행할 코드

- ex) 리스트 요소에 2배씩 곱하기 (직접순회 )

original = [3, 1, 4, 1, 5]
doubled = []

for x in original:
doubled.append(x \* 2)

print(doubled)

# 출력: [6, 2, 8, 2, 10]

# original 리스트의 요소들을 하나씩 x에 할당하고, x\*2를 계산한 결과를 새 리스트 doubled에 추가한다.

# 그러나 요소의 index에 직접 접근할 수 없기에 몇몇 경우엔 제한적일 수 있음

---

**리스트 입력받기**
: 여러 정수를 한 번에 입력받아 list로 저장해야 하는 경우, input()과 map()을 조합하여 활용할 수 있다.

1. 기본구조

리스트이름 = list(map(변환함수, input().split()))

- input().split() :사용자가 입력한 문자열을 공백을 기준으로 분리하여 리스트로 만든다.
- map(변환함수, ...) : 분리된 문자열들을 지정한 함수 (ex:int)에 사용하여 변환한다.
- list(...): map 객체를 리스트로 변환한다.

2. ex) 여러 정수를 한 번에 입력받아 리스트로 저장하기

# 사용자로부터 여러 정수를 입력받아 리스트로 저장

numbers = list(map(int, input().split()))

print(numbers)

# 입력: 10 20 30 40 50

# 출력: [10, 20, 30, 40, 50]

=> 위 예제에선 사용자가 공백으로 구분된 여러 정수를 입력하면, 이를 int 타입으로 변환하여 리스트 numbers에 저장한다.

---

리스트 컴프리헨션이란?
:반복문 (for)와 간단한 표현식을 사용하여, 기존의 list나 반복가능한 객체로부터 새로운 리스트를 짧고 쉽게 만드는 방법이다. 더 짧은 코드로 가독성을 높일 수 있다.

1. 리스트 컴프리헨션의 구조

새로운\_리스트 = [표현식 for 변수 in 시퀀스]

(1) 시퀀스
list :[1,2,3]
range() 함수 : range(3)은 0,1,2를 생성한다.

(2) for 변수 in 시퀀스
: "시퀀스에서 하나씩 꺼내서 변수에 담아"라는 의미로, 일반적으로 사용하는 for문과 유사하다.

- for x in [1,2,3] => 리스트 [1,2,3]의 각 숫자를 하나씩 x에 넣게 된다
- 1번째 반복 : x=1
- 2번째 반복 : x=2
- 3번쨰 반복 : x=3

(3) 표현식
ex)표현식이 x*2면 x에 2를 곱한값을 넣게 되고, x가 1이면 1*2 = 2가 리스트에 추가된다.

ex) 기존 리스트의 숫자에 2를 곱한 new list

arr = [1, 2, 3, 4]
new_arr = [x * 2 for x in arr]
print(new_arr) # 출력: [2, 4, 6, 8]

1. for x in arr 은 arr의 각 숫자를 x에 하나씩 대입
2. x\*2는 x에 2를 곱한 값을 new_arr에 추가함
3. [2,4,6,8] 이라는 새로운 list가 만들어짐

**for문을 사용한 경우**
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
squared.append(num \*\* 2)
print(squared) # 출력: [1, 4, 9, 16, 25]

**list comprehension을 사용한 경우**
numbers = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in numbers]
print(squared) # 출력: [1, 4, 9, 16, 25]

---

**다중 문자열 입력 관리하기**

1. 사용자 입력을 for문으로 처리하기

n = int(input("입력할 문자열의 개수: "))
arr = []
for \_ in range(n):
s = input("문자열 입력: ")
arr.append(s)
print(arr)

설명 :
사용자로 부터 n개의 문자열 숫자 입력받음
빈 리스트 arr 생성
for문 활용하여 n번 반복하면서 각 문자열을 입력받아 arr에 추가
입력된 모든 문자열이 저장된 arr 출력

2. 사용자 입력을 list comprehension으로 처리하기

n = int(input("입력할 문자열의 개수: "))
arr = [input("문자열 입력: ") for _ in range(n)]
print(arr)

설명 :
사용자로 부터 n개의 문자열 숫자 입력받음
리스트 컴프리헨션을 사용해 n번반복 -> arr 리스트에 저장
모든 문자열 저장된 arr 출력

---

i나 num의 정체: "반복 변수 (Iteration Variable)"
이 친구들은 반복하는 '횟수' 그 자체가 아니라, **"이번 바퀴에 내가 처리할 데이터"**를 담아두는 임시 그릇이에요.

for x in [1,2,3]
=> 리스트 [1,2,3]의 각 숫자를 하나씩 x에 넣게 된다
1번쨰 : x=1
2번쨰 : x=2
3번쨰 : x=3

반복하는 횟수?: 이건 보통 range(5)를 썼을 때 0, 1, 2, 3, 4라는 숫자가 튀어나오는 그 '현상'에 가깝고요.

반복 변수 (num): numbers라는 바구니에서 숫자 하나를 꺼내서 잠시 담아두는 이름표입니다.

예시:
for i in range(5): -> 여기서 i는 **"몇 번째 바퀴인지(0, 1, 2, 3, 4)"**를 주로 나타내서 횟수처럼 보입니다.

for num in [10, 20, 30]: -> 여기서 num은 횟수가 아니라 "진짜 데이터 값(10, 20, 30)" 그 자체를 의미합니다.

---

- 연산자 사용 (공백 구분): print(\*my_list)는 리스트의 요소를 분리하여 인자로 전달합니다.

num=[]
print(\*num)

=> [ ] 대괄호 없이 안의 인자들만 출력된다.

---

문제에 이런 말이 있으면,이 도구를 꺼내세요 (Python)
"""일의 자리만 필요해""",% 10 (나머지 연산)
"""마지막 숫자랑 비교해""",리스트[-1] (마이너스 인덱스)
"""딱 N번만 반복해""",for \_ in range(N):
"""홀수인지 짝수인지 봐""",% 2 (2로 나눈 나머지가 0이면 짝수)

---

왜 range(8)이어야 할까요?
이미 있는 데이터: pivot = [2, 5] 라고 입력받는 순간, 리스트의 길이는 이미 2입니다.

우리의 목표: 문제에서 요구한 최종 리스트의 길이는 10입니다.

수학적 계산: 목표(10) - 현재(2) = 남은 횟수(8).

즉, 새로운 숫자를 **8번만 더 만들어서 추가(append)**해야 딱 10개가 맞춰지는 거죠.

🛑 range(10)을 썼을 때 벌어지는 일
채원님이 생각하신 대로 range(10)은 0, 1, 2, ..., 9까지 총 10번 바퀴를 돌립니다.

1회차: [2, 5] -> [2, 5, 7] (길이 3)

2회차: [2, 5, 7] -> [2, 5, 7, 2] (길이 4)

...

10회차: 결국 숫자가 10개 더 추가되어 버려서 최종 길이는 12가 됩니다.
VS Code 정리용 요약
range(N)의 진짜 의미: "안에 있는 코드를 N번 실행해라."

횟수 정하기 공식: (만들고 싶은 총 개수) - (이미 가지고 있는 개수).

주의: range 자체가 숫자를 10까지 세는 게 중요한 게 아니라, 그 안의 append가 몇 번 일어나느냐가 핵심입니다.

---

빈 문자열도 생성할 수 있습니다.

empty = "" # 빈 문자열

문자열의 인덱싱

인덱싱: 특정 문자 접근

문자열에서 특정 문자는 인덱스를 사용하여 접근할 수 있습니다. 인덱스는 0부터 시작합니다.

text = "Python" print(text[0]) # 출력: P print(text[3]) # 출력: h

파이썬은 음수 인덱스도 지원하며, -1부터 시작하여 뒤에서부터 접근합니다.

text = "Python" print(text[-1]) # 출력: n print(text[-4]) # 출력: t

인덱스가 문자열 범위를 초과하면 IndexError 가 발생합니다.

print(text[6]) # 오류 발생

값 수정: 문자열의 변경

문자열은 불변(immutable) 자료형이므로 직접 수정할 수 없습니다.

문자열을 변경하려면 새로운 문자열을 생성해야 합니다.

text = "Python"

특정 문자를 변경하려고 시도 (오류 발생)
text[0] = "J" # 오류 발생

문자열 덧셈 (문자열 연결)

문자열 덧셈은 + 연산자를 사용하여 두 개 이상의 문자열을 연결합니다.

예제 설명: 아래 코드는 두 개의 문자열 str1 과 str2 를 + 연산자로 연결하여 하나의 문장 "Hello, World!"를 생성합니다.

str1 = "Hello, " str2 = "World!" print(str1 + str2) # 출력: Hello, World!

여러 문자열을 연결할 때도 + 연산자를 연달아 사용할 수 있습니다.

단, 문자열과 숫자 등 다른 데이터 타입은 바로 연결할 수 없으므로, 필요시 형변환이 필요합니다.

문자열 곱셈 (문자열 반복)

문자열 곱셈은 \* 연산자를 사용하여 특정 문자열을 지정된 횟수만큼 반복합니다.

예제 설명: 아래 코드는 문자열 str1 을 \* 연산자를 사용해 4번 반복하여 "Hi Hi Hi Hi "와 같이 출력합니다.

str1 = "Hi " print(str1 \* 4) # 출력: Hi Hi Hi Hi

반복 횟수는 정수값으로 지정하며, 음수 값은 사용할 수 없습니다.

문자열 곱셈은 문자열의 패턴을 간편하게 나타낼 수 있어, 반복되는 문자열 생성에 유용합니다.

슬라이싱의 기본 문법

슬라이싱의 기본 문법은 다음과 같습니다.

문자열[start:end]

start : 슬라이싱을 시작할 위치의 인덱스입니다. 이 인덱스는 포함됩니다. end : 슬라이싱을 끝낼 위치의 인덱스입니다. 이 인덱스는 포함되지 않습니다. 즉, end 바로 전에 있는 요소까지만 추출됩니다.

예시:

text = "Python is fun" print(text[1:4]) # 출력: yth

start 혹은 end 생략하기

슬라이싱에서는 start 나 end 를 생략할 수 있습니다.

start 생략: 문자열의 첫 번째 요소(인덱스 0)부터 시작합니다. end 생략: 문자열의 마지막 요소까지를 의미합니다. 둘 모두 생략할 경우 문자열의 처음부터 끝까지 전체를 의미합니다.

text = "Python is fun" print(text[:5]) # 출력: Pytho print(text[2:]) # 출력: thon is fun print(text[:]) # 출력: Python is fun

또한, 음수 인덱스를 사용하여 문자열의 끝에서부터 슬라이싱 범위를 지정할 수도 있습니다.

text = "Python is fun" print(text[-5:]) # 출력: s fun

간격(step) 지정하기

슬라이싱 문법에서는 start , end 외에도 step (간격)을 지정할 수 있습니다. 기본적으로 step 의 값은 1이지만, 2 이상을 주면 해당 간격만큼 건너뛰며 추출합니다.

text = "Python is fun" print(text[::2]) # 출력: Pto sfn

또한 step 에 음수 값을 주면 리스트를 거꾸로 뒤집어서 추출할 수 있습니다.

text = "Python is fun" print(text[::-1]) # 출력: nuf si nohtyP

---

빈 문자열도 생성할 수 있습니다.

empty = "" # 빈 문자열

**문자열의 인덱싱**

인덱싱: 특정 문자 접근
문자열에서 특정 문자는 인덱스를 사용하여 접근할 수 있습니다. 인덱스는 0부터 시작합니다.
text = "Python"
print(text[0]) # 출력: P
print(text[3]) # 출력: h
파이썬은 음수 인덱스도 지원하며, -1부터 시작하여 뒤에서부터 접근합니다.

text = "Python"
print(text[-1]) # 출력: n
print(text[-4]) # 출력: t
인덱스가 문자열 범위를 초과하면 IndexError 가 발생합니다.

print(text[6]) # 오류 발생
값 수정: 문자열의 변경
문자열은 불변(immutable) 자료형이므로 직접 수정할 수 없습니다.

문자열을 변경하려면 새로운 문자열을 생성해야 합니다.

text = "Python"

# 특정 문자를 변경하려고 시도 (오류 발생)

text[0] = "J" # 오류 발생

문자열 덧셈 (문자열 연결)
문자열 덧셈은 + 연산자를 사용하여 두 개 이상의 문자열을 연결합니다.

예제 설명: 아래 코드는 두 개의 문자열 str1 과 str2 를 + 연산자로 연결하여 하나의 문장 "Hello, World!"를 생성합니다.

str1 = "Hello, "
str2 = "World!"
print(str1 + str2) # 출력: Hello, World!
여러 문자열을 연결할 때도 + 연산자를 연달아 사용할 수 있습니다.

단, 문자열과 숫자 등 다른 데이터 타입은 바로 연결할 수 없으므로, 필요시 형변환이 필요합니다.

문자열 곱셈 (문자열 반복)
문자열 곱셈은 \* 연산자를 사용하여 특정 문자열을 지정된 횟수만큼 반복합니다.

예제 설명: 아래 코드는 문자열 str1 을 \* 연산자를 사용해 4번 반복하여 "Hi Hi Hi Hi "와 같이 출력합니다.

str1 = "Hi "
print(str1 \* 4) # 출력: Hi Hi Hi Hi
반복 횟수는 정수값으로 지정하며, 음수 값은 사용할 수 없습니다.

문자열 곱셈은 문자열의 패턴을 간편하게 나타낼 수 있어, 반복되는 문자열 생성에 유용합니다.

---

**슬라이싱의 기본 문법**
슬라이싱의 기본 문법은 다음과 같습니다.

문자열[start:end]
start : 슬라이싱을 시작할 위치의 인덱스입니다. 이 인덱스는 포함됩니다.

end : 슬라이싱을 끝낼 위치의 인덱스입니다. 이 인덱스는 포함되지 않습니다. 즉, end 바로 전에 있는 요소까지만 추출됩니다.

예시:

text = "Python is fun"
print(text[1:4]) # 출력: yth
start 혹은 end 생략하기
슬라이싱에서는 start 나 end 를 생략할 수 있습니다.

start 생략: 문자열의 첫 번째 요소(인덱스 0)부터 시작합니다.

end 생략: 문자열의 마지막 요소까지를 의미합니다.

둘 모두 생략할 경우 문자열의 처음부터 끝까지 전체를 의미합니다.

text = "Python is fun"
print(text[:5]) # 출력: Pytho
print(text[2:]) # 출력: thon is fun
print(text[:]) # 출력: Python is fun
또한, 음수 인덱스를 사용하여 문자열의 끝에서부터 슬라이싱 범위를 지정할 수도 있습니다.

text = "Python is fun"
print(text[-5:]) # 출력: s fun
간격(step) 지정하기
슬라이싱 문법에서는 start , end 외에도 step (간격)을 지정할 수 있습니다. 기본적으로 step 의 값은 1이지만, 2 이상을 주면 해당 간격만큼 건너뛰며 추출합니다.

text = "Python is fun"
print(text[::2]) # 출력: Pto sfn
또한 step 에 음수 값을 주면 리스트를 거꾸로 뒤집어서 추출할 수 있습니다.

text = "Python is fun"
print(text[::-1]) # 출력: nuf si nohtyP

---

**문자열의 주요 메서드**

upper(), lower() : 대소문자 변환

upper() : 문자열의 모든 문자를 대문자로 변환합니다.

lower() : 문자열의 모든 문자를 소문자로 변환합니다.

text = "Python Programming"
print(text.upper()) # 출력: "PYTHON PROGRAMMING"
print(text.lower()) # 출력: "python programming"

**strip(), lstrip(), rstrip() : 공백문자 제거**

**strip() : 문자열 양쪽에 있는 공백문자를 제거합니다. 제거되는 문자로는 공백문자( )뿐만 아니라 줄바꿈 문자 \n, 탭 문자 \t 도 제거됩니다.**

text = " Hello, World! "
print(text.strip()) # 출력: "Hello, World!"

**lstrip() : 문자열의 왼쪽(앞쪽)에서 공백과 지정한 문자를 제거합니다.**

text = " Hello, World! "
print(text.lstrip()) # 출력: "Hello, World! "

**rstrip() : 문자열의 오른쪽(뒤쪽)에서 공백과 지정한 문자를 제거합니다.**

text = " Hello, World! "
print(text.rstrip()) # 출력: " Hello, World!"

참고: strip() 은 양쪽 공백을 모두 제거하지만, 경우에 따라 왼쪽 또는 오른쪽 공백만 제거하는 것이 더 유용할 수 있습니다. 이럴 때 lstrip() 또는 rstrip() 을 사용하는 것이 좋습니다.

**replace() : 특정 문자열 대체**
replace() : 문자열 내에서 특정 부분 문자열을 앞에서부터 확인하여 다른 문자열로 변경합니다.
첫 번째 인자로 찾을 문자열, 두 번째 인자로 대체할 문자열을 지정합니다. 세번째 인자로는 변경 횟수를 지정할 수 있으며, 생략시 대체 가능한 문자열을 전부 변경합니다.

(ex)
text 에서 처음으로 등장하는 부분 문자열 "Hello" 를 "Good" 으로 변경하는 코드

text = "Hello World, Hello Python!"
new_text = text.replace("Hello", "Good", 1)
print(new_text) # 출력: "Good World, Hello Python!"
text 에서 등장하는 모든 부분 문자열 "Hello" 를 "Good" 으로 변경하는 코드

text = "Hello World, Hello Python!"
new_text = text.replace("Hello", "Good")
print(new_text) # 출력: "Good World, Good Python!"

**split() : 문자열 분할**
split() : 문자열을 구분자를 기준으로 분할하여 리스트로 반환합니다. 구분자를 지정하지 않을 시 공백( )을 구분자로 합니다.

sentence = "Python is fun"
words = sentence.split()
print(words) # 출력: ['Python', 'is', 'fun']
구분자 지정: split() 의 인자로 구분자를 지정하면 해당 구분자로 문자열을 나눕니다.

data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits) # 출력: ['apple', 'banana', 'cherry']

---

**input().split() 의 작동 과정 이해하기**
이전까지는 input().split() 을 기계적으로 사용하여 사용자로부터 여러 값을 입력받고 분할하는 방법을 사용했습니다.
이제 split() 메서드의 작동 원리를 자세히 이해함으로써, input().split() 이 어떻게 작동하는지 더 명확하게 이해할 수 있습니다.

예제: 두 개의 수 입력받아 더하기

# 사용자로부터 두 개의 수를 한 줄에 입력받기

numbers = input().split()

# 입력받은 문자열을 정수로 변환

num1 = int(numbers[0])
num2 = int(numbers[1])

# 두 수의 합을 출력

print(f"두 수의 합은 {num1 + num2}입니다.")

작동 과정:

input() 함수가 실행되어 사용자의 입력을 기다립니다. 예를 들어, 사용자가 10 20 을 입력했다고 가정합니다.

입력된 문자열 "10 20" 에 대해 split() 메서드가 호출되어, 공백을 기준으로 분할됩니다. 이 결과 ['10', '20'] 라는 리스트가 생성됩니다.

리스트의 각 요소를 int() 함수를 사용하여 정수로 변환합니다.

변환된 두 수를 더하여 결과를 출력합니다.

---

**join() : 리스트를 문자열로 결합**

join() : 리스트의 요소들을 하나의 문자열로 결합합니다. 각 요소 사이에 지정한 구분자가 삽입됩니다.

공백( )을 구분자로 삽입한 코드

words = ['Python', 'is', 'fun'] sentence = " ".join(words) print(sentence) # 출력: "Python is fun"

쉼표(,)를 구분자로 삽입한 코드

words = ['Apple', 'Grape', 'Mango'] sentence = ",".join(words) print(sentence) # 출력: "Apple,Grape,Mango"

**find() , index() : 문자열 찾기**

find() : 문자열 내에서 특정 문자열을 찾아 그 시작 위치의 인덱스를 반환합니다. 찾는 문자열이 여러번 등장할 시 가장 앞에 오는 문자열의 시작 인덱스를 반환합니다.

text = "Hello, World!" print(text.find("World")) # 출력: 7
print(text.find("Python")) # 출력: -1

index() : 문자열 내에서 특정 문자열의 첫 등장 위치를 찾아 시작 인덱스를 반환합니다. find() 와 달리 찾지 못하면 ValueError 를 발생시킵니다.

text = "Hello, World!" print(text.index("World")) # 출력: 7
print(text.index("Python")) # 오류 발생: ValueError

**count() : 특정 문자열의 개수 세기**

count() : 문자열 내에서 특정 문자열이 몇 번 등장하는지 세어 반환합니다.

text = "banana" print(text.count("a")) # 출력: 3

**in 연산자 : 포함 관계 확인**

in 은 문자열 내에서 특정 문자열이나 문자가 포함되어 있는지 확인하는 연산자입니다. 연산의 결과로 True 또는 False 값을 반환합니다. 사용법:

text = "Python Programming" print("Python" in text) 출력: True
print("python" in text) 출력: False
print("on Program" in text) # 출력: True

위의 예시에서 in 연산자는 "Python" 이라는 문자열이 text 에 포함되어 있는지 확인하고 True를 반환합니다. 반면, "Cpp" 는 text 에 존재하지 않기 때문에 False를 반환합니다.

in 연산자는 메서드가 아니기 때문에 문자열에 대해 in 을 호출하는 형식이 아닙니다. 메서드와 달리 in 은 항상 연산자 로 사용됩니다.

for 문에서 사용하는 for*in* 과는 다름을 주의합니다.

---

**주요 특수 문자와 예시**

\n : 줄 바꿈 (Newline)

multiline_str = "안녕하세요.\n파이썬을 배워봅시다."
print(multiline_str)

출력:

안녕하세요. 파이썬을 배워봅시다.

\t : 탭 (Tab)

tab_str = "이름\t나이\t직업"
print(tab_str)

출력:

이름 나이 직업

\\ : 백슬래시 (Backslash)

path = "C:\Users\홍길동\Documents"
print(path)

출력:

C:\Users\홍길동\Documents

\' : 작은따옴표 (Single Quote)

quote = '그는 말했다, \'안녕하세요\''
print(quote)

출력:

그는 말했다, '안녕하세요'

\" : 큰따옴표 (Double Quote)

quote = "그녀는 말했다, \"파이썬은 재미있어요\""
print(quote)

출력:

그녀는 말했다, "파이썬은 재미있어요"

---

# it's ~ 나 I'm 같은 내부에 작은따옴표 백슬래쉬(\)를 넣어줄 때는 앞에 하나만 넣어줘도 된다 (덮어쓸 필요가 없다)
