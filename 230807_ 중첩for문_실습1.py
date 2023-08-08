# 1 이상의 정수를 입력하면 그 수의 약수를 출력해주는 프로그램(for를 활용)
print("약수를 출력하는 프로그램")
number=0
div=0

while (True) :
    number=int(input("정수를 입력하세요. : "))
    if (number <= 0) :
        print("1이상의 정수를 입력해주세요.")
        continue
    else :
        for i in range(1, number+1) :
            div = number % i
            if (div == 0) :
                print("%d의 약수는 %d" %(number, i))
        break


# while문과 break문을 활용하여 작성
# 수를 입력받아 그 수가 소수인지 판별하는 프로그램 작성
print("\n소수를 출력하는 프로그램")
num=0
dec=0

while(True) :
    num=int(input("정수를 입력하세요. : "))
    if (num == 0) :
        print("Exit")
        break
    else :
        prime = True
        for i in range(2, num) :
            if (num %  i == 0) :
                prime = False
                break

        if (prime and num > 1) :        # 1은 소수가 아님
            print("%d은/는 소수입니다." % num)
        else :
            print("%d은/는 소수가 아닙니다." % num)


# while문을 활용하여 다이아몬드를 출력하는 프로그램
print("\n다이아몬드를 출력하는 프로그램")