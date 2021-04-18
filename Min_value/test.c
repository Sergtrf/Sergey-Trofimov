#include <stdio.h>
#include <math.h>
#include "uniform_mesh_crushing.h"
#define EPS 1e-5
#define pi 3.141593

void test(rr_func f, double a, double b, double expected_res, int expected_err_code, char *message) {
    double res;
    int err_code;
    res = uniform_mesh_crushing(f, a, b, EPS, &err_code);

    if (err_code == LACK_OF_ACCURACY && expected_err_code == LACK_OF_ACCURACY && fabs(res - expected_res) >= EPS) {
	printf("%s\nTest passed!\n\n", message);
        return ;
    } 

    else if (err_code == expected_err_code || fabs(res - expected_res) < EPS) {
        printf("%s\nTest passed!\n\n", message);
        return ;
    }

    else {
        printf("expected result:                       %lf\nresult by uniform mesh crushing method:%lf\n", expected_res, res);
	printf("expected error code:%d\nerror code:         %d\n ", expected_err_code, err_code);
	printf("%s\n******TEST FAILED!******\n\n", message);
    }
}

double f1(double x) {
    return x;
}

double f2(double x) {
    return x*x - 2*x;
}

double f3(double x) {
    return x*x*x + 3*x*x + x - 1;
}

double f4(double x) {
    return cos(x);
}

double f5(double x) {
    return sin(x);
}


double f6(double x) {
    return exp(x);
}

double f7(double x) {
    return pow(x, 5) + 1e+3;
}

double f8(double x) {
    return cos(x) + 2;
}

double f9(double x) {
    return 1/x;
}

int main() {
    test(f1, 10., -20., -1, WRONG_SEGMENT, "Плохой отрезок");
    test(f1, -10., 0., -10., LACK_OF_ACCURACY, "Прямая");
    test(f1, -1e-4, 1e-7, -1e-4, OK_RES, "Прямая с маленьким отрезком");
    test(f2, -3., 4., -1., OK_RES, "Парабола");
    test(f3, -1., 2., -1.08866, OK_RES, "Неприятное значение");
    test(f4, 2., 4., -1., OK_RES, "cos");
    test(f5, -1e+3, 1e+4, -1., OK_RES, "Большой отрезок");
    test(f7, -1., 1., 999., LACK_OF_ACCURACY, "Степенная функция");
    test(f9, -100., -90., -1e-2, LACK_OF_ACCURACY, "Гипербола");
    return 0;
}
