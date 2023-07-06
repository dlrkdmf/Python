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
print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))
    