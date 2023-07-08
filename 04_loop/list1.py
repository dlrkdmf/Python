# 리스트 선언하고 요소에 접근하기
a = [1,2,3,4]
print(a)

# 리스트 기호인 대괄호 [] 안에 들어간 숫자를 인덱스라고 한다
list_a = [22, 32, 103, '문자열', True, False]
print(list_a[0])        # 22
print(list_a[1])        # 32
print(list_a[2])        # 103
print(list_a[1:3])      # [32,103]

# 리스트의 특정 요소 변경
list_a[0] = "변경"
print(list_a)           # ['변경', 32, 103, ...]

# 대괄호 안에 음수를 넣어 뒤에서부터 요소 선택 가능
print(list_a[-1])       # Flase

# 리스트 접근 연산자를 이중으로 사용할 수 있다
print(list_a[3][0])     # 문

# 리스트 안에 리스트 사용가능
list_b = [[1,2,3],[4,5,6],[7,8,9]]
print(list_b[1])        # [4,5,6]

# 리스트 연산자: 연결, 반복, len
list_c = [1,2,3]
list_d = [4,5,6]

# 연결 연산자
print("list_c + list_d :", list_c + list_d)   # list_c + list_d : [1,2,3,4,5,6]

# 반복 연산자
print("list_c * 3 =", list_c * 3)             # list_c * 3 = [1,2,3,1,2,3,1,2,3]

# 리스트 요소 개수 구하기 len()
print("len(list_c) = ", len(list_c))          # len(list_c) = 3

# 리스트에 요소 추가하기 : append, insert
# a.append(요소)
print('# 리스트 뒤에 요소 추가하기')
list_c.append(4)
list_c.append(5)
print(list_c)           # [1, 2, 3, 4, 5]
print()     

# a.insert(위치, 요소)
print('# 리스트 중간에 요소 추가하기')
list_c.insert(0, 10)
print(list_c)           # [10, 1, 2, 3, 4, 5]

# 리스트 연결 연산자와 요소 추가의 차이
list_A = [1,2,3]
list_B = [4,5,6]
print(list_A + list_B)  # [1, 2, 3, 4, 5, 6]
print(list_A)           # [1, 2, 3]  list_A와 list_B에는 어떠한 변화도 없다.
print(list_B)

# a.extend(b)
list_A.extend(list_B)
print(list_A)           # [1, 2, 3, 4, 5, 6]  list_A에 직접적인 변화가 있다.

# 리스트에 요소 제거하기
# 인덱스로 제거하기 : del, pop  -> 요소의 위치를 기반으로 요소를 제거

# 제거 방법[1] - del
del list_a[1]
print("del list_a[1]:", list_a)

# 제거 방법[2] - pop()
list_a.pop(2)
print("pop(2):", list_a)

# 값으로 제거하기 : remove
list_C = [1,2,1,2]
list_C.remove(2)
print(list_C)

# 모두 제거하기 : clear
list_C.clear()
print(list_C)

# 리스트 내부에 있는지 확인하기 : in/not in 연산자
# 형식 
# 값 in 리스트

list_D = [273, 32, 103, 57, 52]
print(273 in list_D)        # True
print(92 in list_D)         # False

print(273 not in list_D)    # Flase
print(92 not in list_D)     # True