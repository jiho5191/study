# 영문 대문자를 한 줄로 입력받아 1번 이상 입력된 각 문자의 개수를 사전 순으로 출력하는 프로그램

alp = input("영문 대문자를 한 줄로 입력하세요. : ")
listV = alp.split()      # 띄어쓰기 기준으로 리스트 생성
listV.sort()             # 리스트 사전 순으로 정렬

print("출력")
for i in listV :
    cntV = listV.count(i)       # i의 개수
    if (cntV > 0):
        print("%s : %d" % (i, cntV))
        for k in range(cntV - 1) :      # i의 개수 - 1 만큼 지워서 i의 값은 하나만 남도록 함
            listV.remove(i)
