#include <stdio.h>
#include <math.h>
#include <locale.h>
#include <list>
#include <iostream>
using namespace std;
// ����������� ���������


int f_1()
{
	int x1, y1, x2, y2; double res;
	cin >> x1 >> y1 >> x2 >> y2;
	

	setlocale(LC_ALL, "Rus");

	res = sqrt(pow(x2 - x1, 2) + (pow(y2 - y1, 2)));

	printf("\n����� �������: %.2lf", res);

	return 0;

}

int f_2()
{
	int a, b, c; double res;
	cin >> a >> b >> c;

	setlocale(LC_ALL, "Rus");

	res = abs(c - b) + abs(c - a);

	printf("\n����� �������� AC � BC: %.2lf", res);

	return 0;
}

int f_3()
{
	int a, b, c; double res;
	cin >> a >> b >> c;

	setlocale(LC_ALL, "Rus");

	res = (c - a) * (b - c);

	printf("\n������������ �������� AC � BC: %.2lf", res);

	return 0;
}

int f_4()
{
	int x1, y1, x2, y2; double res;
	cin >> x1 >> y1 >> x2 >> y2;


	setlocale(LC_ALL, "Rus");

	res = abs(x2 - x1) * abs(y2 - y1);

	printf("\n������� ��������������: %.2lf", res);

	return 0;
}

int f_5()
{
	int x1, y1, x2, y2, x3, y3; double res1, res2, tt;
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;


	setlocale(LC_ALL, "Rus");

	res1 = sqrt(pow(x2 - x1, 2) + (pow(y2 - y1, 2))) + sqrt(pow(x3 - x2, 2) + (pow(y3 - y2, 2))) + sqrt(pow(x1 - x3, 2) + (pow(y1 - y3, 2)));
	tt = res1 / 2;
	res2 = sqrt(tt * (tt - sqrt(pow(x2 - x1, 2) + (pow(y2 - y1, 2)))) * (tt - sqrt(pow(x3 - x2, 2) + (pow(y3 - y2, 2)))) * (tt - sqrt(pow(x1 - x3, 2) + (pow(y1 - y3, 2)))));

	printf("\n�������� ������������: %.2lf", res1);
	printf("\n������� ������������: %.2lf", res2);

	return 0;
}

int main()
{
	int a;
	setlocale(LC_ALL, "Rus");
	printf("�������� ����� �� 1 �� 5\n");
	cin >> a;

	switch (a)
	{
	case 1:
		f_1();
		break;
	case 2:
		f_2();
		break;
	case 3:
		f_3();
		break;
	case 4:
		f_4();
		break;
	case 5:
		f_5();
		break;
	}

	return 0;
}