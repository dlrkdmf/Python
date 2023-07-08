# try except else 구문

# try except else 구문으로 예외를 처리한다
try:
    # 숫자로 변환한다
    number_input_a = int(input("정수 입력> "))
except:
    print("정수를 입력하지 않았습니다")
else:
    # 출력합니다
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)

# finally 구문 -> 예외가 발생하든 발생하지 않든 무조건 실행할 때 사용하는 코드
# try except 구문으로 예외를 처리합니다
try:
    # 숫자로 변환한다
    number_input_a = int(input("정수 입력>"))
    # 출력
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하세요")
else:
    print("예외가 발생하지 않았습니다")
finally:
    print("프로그램이 끝났습니다.")

'''
try, except, finally 구문의 조합
(1) try 구문은 단독으로 사용할 수 없다. 반드시 except 또는 finally 구문과 함께 사용
(2) else 구문은 반드시 except 구문뒤에 사용해야 한다.
'''
# 예제 - 파일이 제대로 닫혔는지 확인하기: closed 속성으로 알 수 있다.
try:
    # 파일을 연다
    file = ipen("info.txt", "w")
    # 여러 가지 처리를 수행
    # 파일을 닫는다.
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 예제 - 파일 처리 중간에 예외 발생
try:
    # 파일을 연다
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    예외.발생()
    # 파일을 닫는다
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

'''
실행결과
name '예외' is not defined
# 파일이 제대로 닫혔는지 확인하기
file.closed: False
'''

# 예제 - finally 구문 사용해 파일 닫기
try:
    # 파일을 연다
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    예외.발생()
    # 파일을 닫는다
    file.close()
except Exception as e:
    print(e)
finally:
    file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
    
# 예제 - try except 구문 끝난 후 파일 닫기
# try except 구문이 끝난 후에 파일을 닫으면 아무 문제가 없다!
try:
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    예외.발생()
except Exception as e:
    print(e)
# 파일 닫기
file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed) 

