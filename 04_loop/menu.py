'''
[문제] 초기 메뉴 구성을 list로 구성한다.

[초기 메뉴판 구성 내용]
면류
* 짜장면, 짬봉, 우동, 울면

식사류 
* 짜장밥, 짬봉밥, 볶음밥

세트메뉴
* set1(탕수육 + 짜장면 + 짜장면)
* set2(탕수육 + 잡채 + 물만두)
'''

Melas = ['짜장면', '짬뽕', '우동', '울면']
# print(Melas)
Noodles = ['자장면', '짬뽕밥', '볶음밥']
SetMenu = [['탕수육', '짜장면', ' 짜장면'], ['탕수육', '잡채', '물만두']]

# 메뉴 중 면류 마지막에 '간짜장'을 추가하고 싶다.
Melas.append('간짜장')
print(Melas)

# 메뉴 중 면류에서 '우동'을 삭제하고 그 자리에 '사천짜장'을 넣고 싶다.
Melas.remove('우동')
print(Melas)

print(Melas.index('울면'))
Melas.insert(Melas.index('울면'), '사천짜장')
print(Melas)

# 메뉴 중 면류와 식사류의 개수를 합한 총 개수는 몇 개인가?
print(len(Melas) + len(Noodles))

# 메뉴 중 면류와 식사류의 메뉴 이름을 정열(거꾸로)하는 작업을 수행한다.
Melas.sort(reverse=True)
Noodles.sort(reverse=True)
print("Melas : ", Melas)
print("Noodles : ", Noodles)

# 메뉴에 새로운 세트 메뉴를 추가한다 (set3(탕수육 + 고추잡채 + 짬뽕))
SetMenu.append(['탕수육','고추잡채','짬뽕'])
print(SetMenu)