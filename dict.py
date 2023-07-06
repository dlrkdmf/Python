# 딕셔너리 선언하기
dict_a = {
    "name" : "어벤져스",
    "type" : "히어로 영화"
}

# 딕셔너리 요소에 접근하기
print(dict_a)
print(dict_a["name"])       # 어벤져스
print(dict_a["type"])       # 히어로 영화

# 딕셔너리 내부의 값에 다양한 자료를 넣을 수도 있다
dict_b = {
    "director" : ["안소니 루소","조 루스"],
    "cast" : ["아이언맨", "타노스", "토르","닥터스트레인지"]
}

print(dict_b["director"])           

# 예제 1
# 딕셔너리 선언 - 주의 : 키를 문자열로 사용할 떄는 반드시 따옴표를 붙여준다.
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredinet" : ["망고", "설탕", "메타중아황산나트륨"],
    "origin" : "필리핀"
}
# 출력
print(dict)
print("name:", dict["name"])                # name: 7D 건조 망고
print("type:", dict["type"])                # type: 당절임

print("ingredinet:", dict["ingredinet"])    # ingredinet: ['망고', '설탕', '메타중아황산나트륨']
print()

# 값 변경
dict["name"] ="8D 건조 망고"
print(dict["name"])

# 딕셔너리에 값 추가하기/제거하기
# 딕셔너리[새로운 키] = 새로운 값
dict["price"] = 5000
print(dict)

# 딕셔너리 요소 제거
del dict["ingredinet"]
print(dict)

# 예제 2 - 아무것도 없는 딕셔너리에 요소를 추가해 출력해보자
# 딕셔너리 선언
dict_a = {}

# 요소 추가 전에 내용 출력해보자
print("요소 추가 이전 :", dict_a)

# 딕셔너리에 요소 추가
dict_a["name"] = "새로운 이름"
dict_a["head"] = "새로운 정신"
dict_a["body"] = "새로운 몸"

# 출력
print("요소 추가 이후:", dict_a)

# 예제 2 - 두 개의 요소를 가진 딕셔너리를 선언하고, 이 두 요소를 제거한 후 내용을 출력해보자
dict_b = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

# 요소 제거 전 내용 출력해보자
print("요소 추가 이전:", dict_b)

# 딕셔너리 요소 제거
del dict_b["name"]
del dict_b["type"]

# 출력
print("요소 제거 이후:", dict_b)

# 딕셔너리 내부에 키가 있는지 확인
# in 키워드
# 딕셔너리 선언
print(dict_a)

# 사용자로부터 입력을 받습니다.
key = input("> 접근하고자 하는 키: ")

# 출력
if key in dict_a:
    print(dict_a[key])
else: 
    print("존재하지 않는 키입니다.")

# get 함수
# 딕셔너리 선언
print(dict_a)

# 존재하지 않는 키에 접근해보자
value = dict_a.get("존재하지 않는 키")
print("값: ",value)

# None 확인 방법
if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
