# 리스트에 적용할 수 있는 기본 함수 : min(), max(), sum()

numbers = [103, 42, 10, 5, 6]
print(min(numbers))     # 5
print(max(numbers))     # 103
print(sum(numbers))     # 166

# reversed() 함수로 리스트 뒤집기

# 리스트를 선언하고 뒤집는다
list_a = [1,2,3,4,5]
list_reversed = reversed(list_a)

# 출력한다
print("# reversed() 함수")
print("reversed([1,2,3,4,5]):", list_reversed)              # <list_reverseiterator object at 0x7f170c8e6400> 
print("list(reversed([1,2,3,4,5]):", list(list_reversed))   # list(reversed([1,2,3,4,5]): [5, 4, 3, 2, 1]
print()

# 반복문을 적용해본다
print("# reversed() 함수와 반복문")
print("for i inreversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-",i)

# enumerate() 함수와 반복문 조합하기
# 변수 선언
example_list = ["요소A", "요소B", "요소C"]

# 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수를 적용해 출력해보자
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환해 출력합니다
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumenrate() 함수 조합해서 사용하기
# enumerate() - 리스트의 요소에 순서를 부여해주는 함수
print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))

# 실행결과
# 0번째 요소는 요소A 입니다.
# 1번째 요소는 요소B 입니다.
# 2번째 요소는 요소C 입니다.

# 딕셔너리의 items() 함수와 반복문 조합하기
#변수를 선언한다.
exam_dict = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}

# 딕셔너리의 items() 함수 결과 출력
print("#딕셔너리의 items() 함수 결과")
print("items():", exam_dict.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print("#딕셔너리의 items() 함수와 반복문 조합하기")

for key, e in exam_dict.items():
    print("dictinanry[{}] = {}".format(key, e))

# 실행결과
# dictinanry[키A] = 값A
# dictinanry[키B] = 값B
# dictinanry[키C] = 값C

# 예제 - 반복문을 활용한 리스트 생성
array = []

for i in range(0,20,2):
    array.append(i*i)

print(array)

# 실행결과
# [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

# 리스트 안에 for문 사용하기
array1 = [i*i for i in range(0,20,2)]
print(array)