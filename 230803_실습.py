# 실습문제 1
print("입력 숫자가 짝수인지 홀수인지 계산하는 프로그램\n")

num=0.0
num2=0
strV=""

num=float(input("실수를 입력하시오 : "))

if (num % 2 == 0) :
    strV="짝"
else :
    strV="홀"

print("입력받은 " + str(num) + "은 " + strV + "수입니다.")


# 실습문제 2
print("\n")
print("윤년 계산 프로그램\n")

year=0
month=0

year=int(input("연도를 입력하세요 : "))
month=int(input("월을 입력하세요 : "))
resultY=""
resultM=0

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
    result="윤년"
    if (month == 2) :
        resultM=29
    elif (month == 4 or month == 6 or month == 9 or month == 11) :
        resultM=30
    
    else :
        resultM=31
        
else :
    result="평년"
    if (month == 2) :
        resultM=28
    elif (month == 4 or month == 6 or month == 9 or month == 11) :
        resultM=30
    else :
        resultM=31

print(str(year) + "년 " + str(month) + "월은 " + resultY + "이고 " + str(resultM) + "일까지 있습니다.")

    
