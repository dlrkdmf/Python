# 튜플은 리스트와 비슷한 자료형이다.

tuple_test = (10,20,30)

print(tuple_test[0])  # 10
print(tuple_test[1])  # 20
print(tuple_test[2])  # 30

# 튜플과 리스트는 요소를 변경할 때 차이가 있다. 
# 튜플은 내부 요소 변경이 불가능하다

# tuple_test[0] = 1 -> Error 발생

# 괄호 없는 튜플
# 리스트와 튜플의 특이한 사용
[a,b] = [10, 20]
(c,d) = (10, 20)

# 출력한다
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# 괄호가 없는 튜플
tuple_test1 = 10, 20, 30,40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test1:", tuple_test1)
print("type(tuple_test1):", type(tuple_test1))
print()

# 괄호가 없는 튜플 활용
a,b,c = 10,20,30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)      
print("b:", b)
print("c:", c)

# 변수의 값을 교환하는 튜플
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)      
print("b:", b)
print()

# 값을 교환합니다.
a, b = b, a
print("# 교환 후 값")
print("a:", a)      
print("b:", b)
print()

# 튜플과 함수
# 여러 개의 값 리턴하기
# 함수 선언
def test():
    return(10, 20)

# 여러 개의 값을 리턴받습니다.
a, b = test()

# 출력합니다
print("a:", a)      
print("b:", b)

# 람다
# 함수의 매개변수로 함수 전달하기
# 매개 변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()

# 간단하게 출력하는 함수
def print_hello():
    print("안녕하세요")

# 조합하기
call_10_times(print_hello)   # print_hello 함수 10번 실행

# filter() 함수와 map() 함수
# map() 함수 -> 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해 주는 함수
# map(함수, 리스트)

# filter() 함수 -> 리스트의 ㅇ소를 함수에 넣고 리턴된 값이 True인 것으로, 새로운 리스트를 구성해 주는 함수
# 예제
# 함수를 선언합니다.
def power(item):
    return item * item
def under_3(item):
    return item < 3

# 변수 선언
list_input_a = [1,2,3,4,5]

# map() 함수를 사용
output_a = map(power, list_input_a)
print("# map함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list_input_a)
print(a)

# filter() 함수를 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))
print()
