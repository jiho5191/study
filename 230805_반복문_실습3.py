# 평균을 구하고 합격, 불합격을 출력하는 프로그램

subject=int(input("입력할 과목 개수(10과목 이하) : "))
sum=0

for i in range(subject) :
    score=int(input("%d. 과목 점수 : " % (i+1)))
    sum+=score

aver=sum/subject

if ( aver > 80 ) :
    print("평균 : %.1f    합격" % aver)
else :
    print("평균 : %.1f    불합격" % aver)