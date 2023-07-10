# 프로그램을 개발하는 동안 강제로 예외를 발생시키는 경우가 있다.
# 예외를 강제로 발생시키는 키워드 - raise

# 예시
# 입력을 받습니다.
number = int(input("정수 입력> "))

# 조건문 사용
if number > 0:
    # 양수일 때: 아직 미구현 상태임
    raise NotImplementedError
else:
    # 음수일 때: 아직 미구현 상태임
    raise NotImplementedError
