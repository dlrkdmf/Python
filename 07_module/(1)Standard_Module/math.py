# math 모듈은 수학과 관련된 기능을 가지고 있다.
import math

math.sin(1)
math.cos(1)
math.tan(1)
math.floor(2.5)  # 내림
math.ceil(2.5)   # 올림

# (1) from 구문
# from 모듈 이름 import 가져오고 싶은 변수 또는 함수
from math import sin,cos,tan,floor,ceil
sin(1)

cos(1)

tan(1)

floor(2.5)

ceil(2.5)

# (2) as 구문 : 모듈의 이름을 짧게 줄여 사용하고 싶을 때
# import 모듈 as 사용하고 싶은 식별자
import math as m
m.sin(1)
m.cos(1)
m.tan(1)

