# URL을 다루는 라이브러리

from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽는다
target = request.urlopen("https://google.com")
output = target.read()  # -> read() : 해당 웹 페이지에 있는 내용을 읽어서 가져옴

print(output)