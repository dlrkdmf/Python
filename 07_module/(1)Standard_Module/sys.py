# 시스템과 관련된 정보를 가지고 있는 모듈 - sys


# 예제
# 모듈을 읽어들인다.
import sys

# 명령 매개변수를 출력한다
print(sys.argv)
print("---")

# 컴퓨터 환경과 관련된 정보를 출력한다
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)


# 프로그램 강제 종료
sys.exit()