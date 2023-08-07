# 평균을 구하고 합격, 불합격을 출력하는 프로그램

subject=0   # 과목 수 입력
sum=0.0     # 총점
score=0.0   # 점수 입력
aver=0.0    # 평균

subject=int(input("입력할 과목 개수(10과목 이하) : "))

if ( subject > 0 and subject < 11 ) :
    for i in range(subject):
        score = float(input("%d. 과목 점수 : " % (i + 1)))
        sum += score

    aver = sum / subject

    if (aver >= 80):
        print("평균 : %.1f    합격" % aver)
    else:
        print("평균 : %.1f    불합격" % aver)
else :
    print("과목 수는 0보다 크고 10이하의 수만 가능합니다.")

"""
# while 문으로 만드는 방법
subject=0   # 과목 수 입력
sum=0.0     # 총점
score=0.0   # 점수 입력
aver=0.0    # 평균
cnt=0

subject=int(input("입력할 과목 개수(10과목 이하) : "))

if ( subject > 0 and subject < 11 ) :
    while (cnt <= subject-1) :
        score=float(input("%d. 과목 점수 : " % (i + 1)))
        sum+=score
        cnt+=1
    aver = sum / subject

    if (aver >= 80):
        print("평균 : %.1f    합격" % aver)
    else:
        print("평균 : %.1f    불합격" % aver)
else :
    print("과목 수는 0보다 크고 10이하의 수만 가능합니다.")
"""
