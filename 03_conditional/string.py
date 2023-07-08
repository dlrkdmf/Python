# if 조건문과 여러 줄 문자열(1)
# 변수 선언
num = int(input("정수 입력> "))
 
# if 조건문으로 홀수 짝수를 구분한다.
if num % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {} 는 짝수입니다.""".format(num,num))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는 홀수입니다.""".format(num,num))

# if 조건문과 긴 문자열
# 변수 선언
number = int(input('정수 입력> '))

# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("입력한 문자열은 {}입니다. \n{}는(은) 짝수입니다.",format(number,number))
else:
    print("입력한 문자열은 {}입니다. \n{}는(은) 홀수입니다.",format(number,number))
