"""
    한 개의 정수를 입력받고, 1부터 입력받은 수까지 (x, x^2)의 형식을
    갖는 딕셔너리를 생성하고 출력하는 프로그램 작성
"""

# for를 사용한 방법
num = 0         # 정수를 입력받을 변수
dicV = {}       # 딕셔너리 공간

num = int(input("정수를 입력하세요 : "))

for i in range(num) :
    dicV[i + 1] = (i + 1) ** 2

print("사전에 입력된 값\n%s" % str(dicV))

# while을 사용한 방법
num1 = 0
cntV = 0
dicV1 = dict()

num1 = int(input("정수를 입력하세요 : "))

while (cntV <= num1) :
    dicV1[cntV] = cntV ** 2
    # 같은 의미로 사용가능 --> dicV[cntV] = cntV * cntV
    cntV += 1

print("사전에 입력된 값\n%s" % str(dicV1))
