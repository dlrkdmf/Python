'''
try:
    예외가 발생할 수 있는 구문
except 예외의 종류 as 예외 객체를 활용할 변수 이름:
    예외가 발생했을 때 실행할 구문
'''

# 예외 객체
try:
    number_input_a = int(input("정수입력 >"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except Exception as exception:
    # 예외 객체를 출력해보자
    print("type(exception):", type(exception))
    print("exception:", exception)

# 예외 구분하기
# 예제 - 여러가지 예외가 발생할 수 있는 코드
# 변수를 선언한다.