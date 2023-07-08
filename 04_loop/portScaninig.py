portlist = []
portlist.append(21)
portlist.append(22)
# print(portlist)
portlist.append(80)
portlist.append(443)
portlist.append(25)
print(portlist)

# 포트 스캔 결과 중 특정 포트 이전의 포트 개수
pos = portlist.index(80)
print(pos)
print("[+] There are " + str(pos) + " port to scan before 80.")

# 포트 스캐닝할 포트 번호 삭제
portlist.remove(443)
cnt = len(portlist)
print("[+] Scanning" + str(cnt) + "Total Ports.")
