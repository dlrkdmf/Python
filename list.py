'''
[EX] 행열을 간단하게 표시하기
다음 행열을 Python list로 표시하시오.
'''
metrix = [[1,2,3], [4,5,6], [7,8,9]]
print(metrix)

'''
[EX] 우리 가족에 대해서
우리 가족의 구성(!!! 대장은 mother !!!)
'''
family = ['mother','father','sister']

# 우리 가족은 몇 명?
print(family)
print(len(family))

# 가족 중 넘버(Number) 3은 누구지?
print(family[2])

# 해외로 동생이 어학연수를 갔다면 한국에 남아있는 가족은?
family.remove('sister')
print(family)


