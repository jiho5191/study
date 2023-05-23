#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int year = 2019, mon;
	int total = 1;
	int month[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	int i;

	printf("월 입력 : ");
	scanf("%d", &mon);

	for (i = 2018; i < year; i++) {
		total += 365;
	}

	for (i = 0; i < mon - 1; i++) {
		total += month[i];
	}

	printf("\n\t\t\t%d월\n", mon);
	printf("---------------------------------------------------\n");
	printf("일\t월\t화\t수\t목\t금\t토\n");
	printf("---------------------------------------------------\n");

	//1년부터 2019년까지의 총 일수를 7로 나누어 나머지가 0이면 일요일, 1이면 월요일이 되도록 만드는 함수
	int start, end; //1일이 시작하는 자리, 마지막 날이 끝나는 자리
	start = total % 7;
	end = month[mon - 1];
	for (i = 0; i < start; i++) {
		printf("\t");
	}
	for (i = 1; i <= end; i++) {
		printf("%2d\t", i);
		if ((i + start) % 7 == 0) {
			printf("\n");
		}
	}


	return 0;
}