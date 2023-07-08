# 기본적인 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# def 함수 이름(매개변수, 매개변수, ...)
#     문장

# 매개변수의 기본
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요",5)

# 실행결과
# 안녕하세요
# 안녕하세요
# 안녕하세요
# 안녕하세요
# 안녕하세요

# 매개변수와 관련된 TypeError - 매개변수를 두 개 지정했는데 하나만 넣었을때

# 가변 매개변수 함수
def print_n_values(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        print()
# 함수 호출
print_n_values(3, "안녕하세요", "즐거운","파이썬 프로그래밍")

# 기본 매개변수
def print_n_times1(value,n=2):
    # n번 반복
    for i in range(n):
        print(value)
# 함수 호출
print_n_times1("안녕")

# 실행 결과
# 안녕
# 안녕

# 키워드 매개변수
# while 반복문 사용
'''
while True:
print(".", end="")  # end="" -> 키워드 매개변수
'''

# 예제
def print_n_times2(*values, n=2):
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        print()
# 함수 호출
print_n_times2("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

# 기본 매개변수 중에서 필요한 값만 입력하기
def test(a, b=10, c=100):
    print(a+b+c)

# 1) 기본 형태
test(10,20,30)              # 60

# 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)    # 310

# 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b=200)    # 310

# 4) 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=100)             # 220

# 리턴 -> 함수를 실행했던 위치로 돌아가라, 함수를 여기서 끝내라
# 자료없이 리턴하기
def return_test():
    print(" A 위치입니다 ")
    return
    print(" B 위치입니다 ")

# 함수 호출
return_test()

# 실행결과 
# A 위치입니다 

# 자료와 함께 리턴하기
def return_test1():
    return 100

value = return_test1
print(value)                # 100

# 아무것도 리턴하지 않기
def return_test2():
    return

value = return_test2
print(value)                # None

# 기본적인 함수의 활용
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output
# 함수 호출
print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))