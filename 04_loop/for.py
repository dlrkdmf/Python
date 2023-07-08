# for 반복문 - 범위
# 매개변수에 숫자 한 개 넣는 방법 - range(A)

# 매개변수에 숫자 두 개 넣는 방법 - range(A,B)

# 매개변수에 숫자 세 개 넣는 방법 - range(A,B,C)

a = range(5)
print(a)        # range(0,5)

# range 내부 값 확인하기
print(list(range(10)))      # [0,1,2,3,4,5,6,7,8,9]

# 매개변수에 숫자 두 개 넣은 범위
print(list(range(5,10)))    # [5,6,7,8,9]

# 매개변수에 숫자 세 개 넣은 범위
print(list(range(0,10,2)))  # [0,2,4,6,8,9]

print(list(range(0,10,3)))  # [0,3,6,9]

# 범위를 만들 때 매개변수 내부에 수식을 사용하는 경우도 있다
a = range(0,10+1)
print(list(a))              # [0,1,2,3,4,5,6,7,8,9,10]

# 수식에 나누기를 사용한 경우
n = 10
# a = range(0, n /2)          # TypeError 발생

b = range(0, int(n/2))
print(list(b))                # [0,1,2,3,4]

# for 반복문: 범위와 함께 사용하기
for i in range(5):
    print(str(i) + "=반복 변수")
print()

for i in range(5,10):
    print(str(i) + "=반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + "=반복 변수")
print()                             


# for 반복문: 리스트와 함께 사용하기
array = [273, 32,103, 57, 52]

# 리스트에 반복문을 적용한다.
for element in array:
    print(element)

# for 반복문: 리스트와 범위 조합하기
# 리스트 선언
array_a = [273, 32, 103, 58, 52]
for i in range(len(array_a)):
    print("{}번째 반복: {}".format(i, array_a[i]))

# for 반복문: 반대로 반복하기
# 역반복문
for i in range(4, 0 -1, -1):
    print("현재 반복 변수: {}".format(i))

# for 반복문: 반대로 반복하기(2)
# 역반복문
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
    
# for 반복문: 딕셔너리와 함께 사용하기
# 딕셔너리 선언
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredinet" : ["망고", "설탕", "메타중아황산나트륨"],
    "origin" : "필리핀"
}

# for 반복문 사용
for key in dict:
    print(key, ":", dict[key])
