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
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리한다
try:
    # 숫자를 입력받는다
    number_input = int(input("정수 입력 > "))  
    # 리스트의 요소를 출력합니다
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    # 예외 객체를 출력해본다
    print("type(exception):", type(exception))
    print("exception:", exception)
'''
실행결과
(1) 정수로 변환될 수 없는 값을 입력했을 때 : ValueError
(2) 정수를 입력하지만, 리스트의 길이를 넘는 인덱스를 입력한 경우 : IndexError
(3) 정상적으로 정수를 입력한 경우 : 예외 발생 x
'''
# 예제 - 예외 구분하기 
# 변수를 선언한다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리한다
try:
    # 숫자를 입력받는다
    number_input = int(input("정수 입력 > "))  
    # 리스트의 요소를 출력합니다
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    # ValueError가 발생하는 경우
    print("정수를 입력해주세요!")
except IndexError:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")

# 예외 구분 구문과 예외 객체
# 변수를 선언한다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리한다
try:
    # 숫자를 입력받는다
    number_input = int(input("정수 입력 > "))  
    # 리스트의 요소를 출력합니다
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
# ValueError가 발생하는 경우
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError as exception:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)

# 모든 예외 잡기 
# 예제 - 예외 처리를 했지만 예외를 못 잡는 경우
# 변수를 선언한다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리한다
try:
    # 숫자를 입력받는다
    number_input = int(input("정수 입력 > "))  
    # 리스트의 요소를 출력합니다
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()  # 예상하지 못한 예외 발생 -> '예외'라는 이름의 변수가 없으므로 NameError가 발생한다.
except ValueError as exception:
# ValueError가 발생하는 경우
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError as exception:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)

# 예제 - 모든 예외 잡기
# 변수 선언
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외를 처리한다
try:
    # 숫자를 입력받는다
    number_input = int(input("정수 입력 > "))  
    # 리스트의 요소를 출력합니다
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()  # 예상하지 못한 예외 발생
except ValueError as exception:
# ValueError가 발생하는 경우
    print("정수를 입력해주세요!")
    print("exception:", exception)
except IndexError as exception:
    # IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)
except Exception as exception:
    # 이외의 예외가 발생한 경우
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print("exception:", exception)
