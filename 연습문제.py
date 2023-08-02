
# 연습문제 1
iot=int(input("IoT 점수 : "))
ai=int(input("인공지능 점수 : "))
ml=int(input("머신러닝 점수 : "))
total=iot+ai+ml
aver=total/3
print("\n과목의 총점 : %d\n과목의 평균 : %d\n" % (total, aver))


# 연습문제 2
print("아이스크림, 라면, 과자, 빵의 총 금액\n")
icecream=0   # 아이스크림 개수
noodle=0     # 라면 개수
snack=0      # 과자 개수
bread=0      # 빵 개수

totalP=0 # 구매한 내역의 총 금액

icecreamP=1000  # 아이스크림 가격
noodleP=1500    # 라면 가격
snackP=2000     # 과자 가격
breadP=1500     # 빵 가격

icecream=int(input("아이스크림 개수 : "))
noodle=int(input("라면  개수 : "))
snack=int(input("과자 개수 : "))
bread=int(input("빵 개수 : "))

totalP=(icecream*icecreamP)+(noodle*noodleP)+(snack*snackP)+(bread*breadP)

print("총 금액 : " + str(totalP))
print("총 금액 : ", totalP)
print("총 금액 %d원 입니다.\n" % totalP)


# 연습문제 3
from math import pi
print("각도를 라디안으로 변환하여 출력하는 프로그램\n")
Degree=float(input("각도 : "))
Radian=Degree*(pi/180)
print("라디안 : %f\n" % Radian)


# 연습문제 4
print("원기둥의 표면 부피와 면적을 구하는 프로그램\n")

# 변수 생성
pi=3.14
h=0.0   # 높이
r=0     # 반지름

V=0.0   # 표면 부피
A=0.0   # 표면 면적

h=float(input("높이 입력(실수) : "))
r=int(input("반지름 입력(정수) : "))

V = pi * h * (r ** 2)
A = (( 2 * pi * r ) * h ) + (( pi * ( r **2 ) *2))

print("부피 : %.2f\n면적 : %.2f\n" % (V,A))
