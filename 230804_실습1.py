# 실습문제 1
print("동물을 영어로 출력하는 프로그램\n")
print("1.고양이   2.강아지   3.햄스터   4.토끼")
answer=int(input("번역하고 싶은 동물의 숫자를 입력하세요. : "))
engName=""

if (answer == 1) :
    engName="Cat"
elif (answer == 2) :
    engName="Puppy"
elif (answer == 3) :
    engName="Hamster"
elif (answer == 4) :
    engName="Rabbit"
else :
    engName="I Don\'t konw"

print( str(answer) + "번의 영어 이름은 " + engName)
print("\n")


# 실습문제 2
print("최대, 최소, 합계, 평균을 계산하는 프로그램")
"""
num=[0,0,0]

for i in range(3) :
    num[i]=int(input("원하는 정수를 입력하세요. : "))

sum=num[0]+num[1]+num[2]
aver=sum/3
maxNum=0
minNum=99999

for k in range(3) :
    if (maxNum<num[k]) :
        maxNum=num[k]
    if (minNum>num[k]) :
        minNum=num[k]
"""

num1=int(input("원하는 정수를 입력하세요. : "))
num2=int(input("원하는 정수를 입력하세요. : "))
num3=int(input("원하는 정수를 입력하세요. : "))

maxN=num1
minN=num1

if (maxN <= num2) :
    maxN = num2
if (maxN <= num3) :
    maxN = num3
if (minN >= num2) :
    minN = num2
if (minN >= num3) :
    minN = num3

sum = num1 + num2 + num3
aver = sum / 3

print("최대 : %d    최소 : %d    합계 : %d    평균 : %.1f" % (maxN, minN, sum, aver))