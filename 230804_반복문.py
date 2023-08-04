"""
    Python에서 사용되는 반복문의 종류 2가지
    1) for
        - 사용 : 정해진 횟수
        - 문법
            for 변수 in (4가지 방법) :
                실행문장
        - 4가지 방법
            (1) 문자열
            (2) 문자열 변수
            (3) 참조형 변수(리스트, 튜플, 셋, 딕셔너리)
            (4) range()     -> 안의 값은 항상 정수!!
                ※ range( 시작, 종료, 증감값 )
                    -> 원하는 위치부터 총료 -1까지 증감값에 따라 반복
                    -> 종료값 -1 까지 출력하기 때문에 종료값 +1 해줘야 함
                ※ range( 시작, 종료 )         -> 시작부터 종료 -1까지 1씩 증가
                ※ range( 종료 )              -> 0부터 종료 -1까지 1씩 증가

    2) while
        - 사용 : 조건에 만족할 때
"""

i=""
strV="개강하기 싫어요"

for i in strV :
    print(strV, end=", ")

print("종료")

# 1부터 10 사이의 정수 중 짝수만 출력 (3가지 방법)
for i in range(1, 11) :
    if (i % 2 == 0 ) :
        print(i)

print("\n")
for k in range(2, 11, 2) :
    print(k)

print("\n")
for j in range(11) :
    if (j > 0 and j % 2 == 0) :
        print(j)