# 운영체제와 관련된 기능을 가진 모듈

# 예제
# 모듈을 읽어들인다
import os
# 기본 정보를 몇 개 출력해보자
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거[폴더가 비어있을 때만 제거 가능]
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성하고 + 파일이름을 변경한다
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일 제거
os.remove("new.txt")

# 시스템 명령어 실행
os.system("dir") # -> os.system() 함수는 명령어를 그냥 실행하기 때문에 주의해서 사용해야한다.