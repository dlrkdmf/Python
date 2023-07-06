# while 반복문 - 조건이 참인 동안 문장을 계속 반복
'''
while True:
    print(".", end= "")
'''

# while 반복문: for 반복문처럼 사용하기
# 반복변수를 기반으로 반복하기
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# whie 반복문: 상태를 기반으로 반복하기
# 변수 선언
list_test = [1,2,1,2]
value = 2

# list_test 내부에 value가 있다면 반복
while value in list_test:
    list_test.remove(value)

# 출력
print(list_test)        # [1,1] - 리스트 내부에 있는 모든 2가 제거될 때까지 반복되기 때문에 2가 모두 제거된 결과가 출력된다.
'''
# while 반복문: 시간을 기반으로 반복하기
# 시간과 관련된 기능 가져오기
import time

# 변수 선언
number = 5

# 5초 동안 반복
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

# 출력
print("5초 동안 {}번 반복했습니다." .format(number))
'''
# while 반복문: break 키워드/continue 키워드
# 변수 선언
i = 0

# 무한 반복
while True:
    # 몇 번째 반복인지 출력
    print("{}번째 반복입니다.".format(i))
    i = i + 1
    
    # 반복 종료
    input_text = input("> 종료하시겠습니끼(y/n): ")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다")
        break

# 변수 선언
numbers = [ 5,15,16,20,7]

# 반복을 돌립니다
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue

    # 출력
    print(number)
