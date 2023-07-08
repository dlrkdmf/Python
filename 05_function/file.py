# 파일을 열 때는 open() 함수를 사용한다
# 파일을 닫을 때는 close() 함수를 사용한다

# 파일 열고 닫기 예제
# 파일을 연다.
file = open("basic.txt", "w")

# 파일에 텍스트를 씁니다.
file.write("Hello Python Programming")

# 파일을 닫습니다.
file.close()  # -> 프로그램을 실행하면 같은 폴더에 "basic.txt"라는 파일이 생성된다.

# with 키워드  -> 파일을 열고 닫지 않는 실수를 방지하기 위해 생긴 기능
# 파일을 연다
with open("basic.txt", "w") as file:
    # 파일에 텍스트를 쓴다
    file.write("Hello Python")

# 텍스트 읽기
# 예제
# 파일을 연다
with open("basic.txt", "r") as file:
    # 파일을 읽고 출력한다
    contents = file.read()
print(contents) # -> Hello Python

# 텍스트 한 줄씩 읽기
# 랜덤하게 1000명의 키와 몸무게 만들기

# 랜덤한 숫자를 만들기 위해 가져온다.
import random

# 간단한 한글 리스트를 만든다.
hanguls = list("가나다라마바사")

# 파일을 쓰기 모드로 연다.
with open("info.txt", "w")as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성한다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)  # 숫자 범위 40 ~ 100
        height = random.randrange(140, 200) # 숫자 범위 140 ~ 200
        # 텍스트를 쓴다
        file.write("{}, {}, {}\n".format(name, weight, height))

# 반복문으로 파일 한 줄씩 읽기
with open("info.txt", "r")as file:
    for line in file:
        # 변수를 선언한다
        (name, weight, height) = line.strip().split(",")

        # 데이터가 문제없는지 확인, 문제가 있으면 지나감
        if (not name) or (not weight) or (not height):
            continue
        # 결과를 계산한다
        bmi = int(weight) / ((int(height) / 100 ) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        # 출력한다
        print("\n".join([
            "이름 : {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()




