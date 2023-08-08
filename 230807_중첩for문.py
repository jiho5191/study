"""
    break 멈추다
    continue 계속
    -> 반복문에서 사용
"""

# 중첩 for문 실습
# 문자열을 입력받아 모음을 없애고 자음만 출력하는 프로그램

strV=""                 # 문자열을 입력받기 위한 변수
vowels="aeiouAEIOU"     # 모음 문자열
strV_1=""               # 완성된 문자열

strV=input("영어 문자열을 입력하세요. : ")

for i in strV :
    # in --> 포함된 것을 확인
    # not in --> 포함되지 않은 것을 확인
    if ( i in vowels ) :
        print("모음 : " + i)
        continue            # 모음이라면 반복문 처음으로 이동
        print("1")          # continue 다음 문장은 실행하지 않는지 확인
    else :
        strV_1 += i         # 자음이라면 문자열 추가

print("모음을 제외한 문자열 : %s" % strV_1)


# 반복문을 탈출시키는 break문
# break문으로 첫 번째 수에 0이 입력될 때 자동으로 종료되는 프로그램

num1=0
num2=0
sumV=0

while (True) :
    num1=int(input("첫 번째 정수를 입력하세요 : "))
    if (num1 == 0) :
        print("첫 번째 정수가 0이 입력되어 프로그램을 종료합니다.")
        break
    num2=int(input("두 번째 정수를 입력하세요 : "))
    sumV=num1+num2
    print("%d + %d = %d" % (num1,num2,sumV))