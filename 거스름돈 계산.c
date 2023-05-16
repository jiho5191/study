#include <stdio.h>

int main(void)
{
	int price, given, won1, won2, won3, won4;
	printf("물건의 가격:");
	scanf_s("%d", &price);
	printf("고객에게서 받은 화폐:");
	scanf_s("%d", &given);
	won1 = (given - price) / 10000;
	won2 = (given - price - won1*10000) / 1000;
	won3 = (given - price - won1*10000 - won2*1000) / 100;
	won4 = (given - price - won1*10000 - won2*1000 - won3*100) / 10;
	printf("고객에게 내어줄 잔돈\n");
	printf("만 원권: %d\n", won1);
	printf("천 원권: %d\n", won2);
	printf("백 원: %d\n", won3);
	printf("십 원: %d\n", won4);

	return 0;
}