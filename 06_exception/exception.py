'''
실행 전에 발생하는 오류 : 구문 오류(Syntax Error)
프로그램 실행 중에 발생하는 오류 : 예외(Exception) 또는 런타임 오류

구문오류와 예외의 차이를 설명해라
-> 구문오류는 문법적인 오류로 프로그램이 실행이 안되는 오류
    예외는 프로그램 실행 중에 발생하는 오류로 try구문으로 처리할 수 있다.  
'''

# 조건문으로 예외 처리하기
# 숫자를 입력받습니다
user_input_a = input("정수 입력> ")

# 사용자 입력이 숫자로만 구성되어 있을 때
if user_input_a.isdigit():
    # 숫자로 변환합니다.
    number_input_a = int(user_input_a)
    # 출력합니다
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")
# 정수를 입력하면 정상적으로 값을 반환하고
# 문자열을 입력하면 isdigit() 함수를 사용하여 else 구문 쪽으로 들어가서 "정수를 입력하지 않았습니다"라는 문자열을 출력한다.

# try except 구문
# 예제
try:
    # 숫자로 변환합니다
    number_input_a = int(input("정수 입력> ")) # 예외가 발생할 가능성이 있는 구문
    # 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a) 
except:
    print("무언가 잘못되었습니다.") # 예외가 발생했을 때 실행할 구문

# try except 구문과 pass 키워드 조합하기
# 숫자로 변환되는 것들만 리스트에 넣기
# 변수를 선언한다
list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복을 적용한다
list_number = []
for item in list_input_a:
    # 숫자로 변환해서 리스트에 추가한다
    try:
        float(item) 
        list_number.append(item)
    except:
        pass
# 출력한다
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다".format(list_number))

# try 구문 내에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

# test() 함수를 호출한다
test()

