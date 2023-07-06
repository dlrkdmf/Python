# for 반복문
# for 반복문: 리스트와 함께 사용하기
array = [273, 32,103, 57, 52]

# 리스트에 반복문을 적용한다.
for element in array:
    print(element)

# for 반복문: 딕셔너리와 함께 사용하기
# 딕셔너리 선언
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredinet" : ["망고", "설탕", "메타중아황산나트륨"],
    "origin" : "필리핀"
}

# for 반복문 사용
for key in dict:
    print(key, ":", dict[key])