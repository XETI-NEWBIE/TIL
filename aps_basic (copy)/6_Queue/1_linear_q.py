
# 선형 큐
n=3
que = [0]*n
front = rear = -1

def enqueue(item):
    global rear
    # 꽉 찬걸 예상하지 못하고 enqueue했을 경우
    # 1. 큐의 크기를 잘못예측함
    # 2. 구현 실수로 너무 많이 enqueue
    if is_full():
        print("Queue_Full")
    else:
        # .append() 구현도 가능
        rear = rear+1
        q[rear] = item

def dequeue():
    global front
    if is_empty():
        print("Queue_Empty")
    else:
        # q.pop(0) 형태도 가능
        front = front + 1
        return q[front]

# 공백 상태 : front == rear
# 포화 상태 : rear == n-1 (n : 배열의 크기, n-1 : 배열 마지막 인덱스)
def is_empty():
    return front == rear

def is_full():
    return rear==len(q) - 1

# 선형 큐 : 잘못된 포화상태 인식 문제점 有
# 원형 큐 : 선형 큐의 공간 낭비를 위해 끝과 시작이 연결된 구조


# 선형 큐 연습 

n=6
que = [0]*n
front = rear = -1

#enqueue()
rear+=1
que[rear]=1 #enqueue(1)

rear+=1
que[rear]=2 #enqueue(2)

rear+=1
que[rear]=3 #enqueue(3)

rear+=1
que[rear]=4 #enqueue(4)

rear+=1
que[rear]=5 #enqueue(5)

rear+=1
que[rear]=6 #enqueue(6)

while front != rear:    #front == near : 큐가 비어있는 상태
    front += 1
    tmp = que[front]
    print(tmp)

## 쉬운 방법 (야매너낌)
q =  []
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)

print(q.pop(0))
print(q.pop())
