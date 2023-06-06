#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>

void period(void);                                        //주차 기간 함수
void parking(void);                                      //단기,장기 주차 구분 함수
void car(void);                                          //차량 구분 함수
void reduction(void);                                    //요금감면 구분 함수
void parking_fee(void);                                   //주차 요금 계산 함수
int parking_period;                                      //단기, 장기 주차를 구분할 변수
int num;                                                 //소형, 대형을 구분할 변수
int reduct;                                              //요금감면을 구분할 변수
int tm_day, tm_hour, tm_min;                             // 시간 값을 저장할 변수

int main() {
	printf("주차 요금 계산기\n\n");
	period();
	parking();
	if (parking_period == 2) { //단기주차 차량은 승용차 밖에 없기 때문에 묻지 않고 넘어간다.
		printf("\n승용차, 15인 이하 버스, 최대적재량 1톤 이하 화물차는 소형 차량으로 구분됩니다.\n");
		car();
	}
	else {
		num = 1;
	}
	reduction();
	parking_fee();

	return 0;
}

void parking(void) {
	printf("\n1일 이상 장기주차 차량은 장기주차장을 이용하여 주시기 바랍니다.\n");
	printf("1.단기주차(승용차 전용)   2.장기주차  : ");
	scanf("%d", &parking_period);
	if ((parking_period != 1) && (parking_period != 2)) {
		printf("다시 입력해주세요\n");
		parking();
	}
}

void car(void) {
	printf("1.소형   2.대형  : ");
	scanf("%d", &num);
	if ((num != 1) && (num != 2)) {
		printf("다시 입력해주세요\n");
		car();
	}
}

void period(void) {
	time_t start, end;
	double diff;

	// time1 입력
	struct tm user_stime;
	int fy, fm, fd, fh, fmin;

	// time1값 입력
	printf("들어올 날짜를 입력해주세요 (예:yyyy mm dd) : ");
	scanf_s("%d %d %d", &fy, &fm, &fd);
	printf("들어올 시간을 입력해주세요 (예:hh mm) : ");
	scanf_s("%d %d", &fh, &fmin);


	// time1 구조체에 대입
	user_stime.tm_year = fy - 1900; // 년도가 1900년부터 시작하기 때문
	user_stime.tm_mon = fm - 1; //월이 0부터 시작하기 때문
	user_stime.tm_mday = fd;
	user_stime.tm_hour = fh;
	user_stime.tm_min = fmin;
	user_stime.tm_isdst = 0; //썸머타임 사용안함

	// time2 입력
	struct tm user;
	int sy, sm, sd, sh, smin;

	// time2값 입력
	printf("나갈 날짜를 입력해주세요 (예:yyyy mm dd) :  ");
	scanf_s("%d %d %d", &sy, &sm, &sd);
	printf("나갈 시간을 입력해주세요 (예:hh mm) : ");
	scanf_s("%d %d", &sh, &smin);

	// time2 구조체에 대입
	user.tm_year = sy - 1900; // 년도가 1900년부터 시작하기 때문
	user.tm_mon = sm - 1; //월이 0부터 시작하기 때문
	user.tm_mday = sd;
	user.tm_hour = sh;
	user.tm_min = smin;
	user.tm_isdst = 0; //썸머타임 사용안함

	start = mktime(&user_stime);
	end = mktime(&user);

	// 시간 차이 계산
	diff = difftime(end, start);

	// 일 계산
	tm_day = diff / (60 * 60 * 24);
	diff = diff - (tm_day * 60 * 60 * 24);

	// 시간 계산
	tm_hour = diff / (60 * 60);
	diff = diff - (tm_hour * 60 * 60);

	// 분 계산
	tm_min = diff / 60;
	diff = diff - (tm_min * 60);
}

void reduction(void) {
	printf("\n1.해당사항 없음   2.경차/장애인/국가유공자/다자녀가구/저공해자동차 1종,2종   3.저공해자동차 3종  : ");
	scanf("%d", &reduct);
	if ((reduct != 1) && (reduct != 2) && (reduct != 3)) {
		printf("다시 입력해주세요\n");
		reduction();
	}
}

void parking_fee(void) {
	int fee = 0; //총 계산 결과

	//단기주차일 때, 주차요금 계산
	if (parking_period == 1) {
		fee = 1200;     //기본 30분 요금 1200원

		for (int n = 0; n < tm_day; n++) {
			fee += 24000;     //하루 최대 주차요금은 24000원이다.
		}

		if (tm_hour <= 10) {
			for (int n = 0; n < tm_hour; n++) {
				fee += 2400;
			}

			if (tm_min == 0) fee;
			else if (tm_min <= 15) {
				fee += 600;
			}
			else if (tm_min <= 30) {
				fee += 1200;
			}
			else if (tm_min <= 45) {
				fee += 1800;
			}
			else if (tm_min <= 60) {
				fee += 2400;
			}
		}
		else fee += 24000;

		if ((tm_hour != 0) || (tm_day != 0)) {
			fee = fee - 1200; //하루 30분 기본 요금
		}
	}

	//장기주차일 때, 주차요금 계산
	else if (parking_period == 2) {
		//소형 기준
		if (num == 1) {
			for (int n = 0; n < tm_day; n++) {
				fee += 9000;     //하루 최대 주차요금은 9000원이다.
			}

			if (tm_hour <= 9) {
				for (int n = 0; n < tm_hour; n++) {     //시간당 1000원
					fee += 1000;
				}

				if (tm_min == 0) fee;
				else if (tm_min <= 60) {
					fee += 1000;
				}
			}
			else fee += 9000;
		}
		//대형 기준
		else if (num == 2) {
			for (int n = 0; n < tm_day; n++) {
				fee += 12000;     //하루 최대 주차요금은 12000원이다.
			}

			if (tm_hour <= 5) {
				for (int n = 0; n < tm_hour; n++) {
					fee += 2400;
				}

				if (tm_min == 0) fee;
				else if (tm_min <= 30) {
					fee += 1200;
				}
				else if (tm_min <= 60) {     //30분당 1200원
					fee += 2400;
				}
			}
			else fee += 12000;
		}
	}

	//감면조건을 포함한 주차요금 계산
	if (reduct == 1) {
		printf("\n예상 주차요금은 %d원 입니다.\n", fee);
	}
	else if (reduct == 2) {
		fee = fee / 2;     //50% 할인
		printf("\n예상 주차요금은 %d원 입니다.\n", fee);
	}
	else if (reduct == 3) {
		fee = fee * 8 / 10;     //20% 할인
		printf("\n예상 주차요금은 %d원 입니다.\n", fee);
	}
}