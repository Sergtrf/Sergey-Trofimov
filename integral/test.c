#include <stdio.h>
#include <math.h>
#include "trapezium_integral.h"
#define EPS 1e-3
#define pi 3.141593

void test(rr_func f, double a, double b, double expected_res, int expected_err_code, char *message) {
    double res;
    int err_code;
    res = integral(f, a, b, EPS, &err_code);

    if (err_code == OK_RES && expected_err_code == LACK_OF_ACCURACY && fabs(res - expected_res) >= EPS) {
        printf("%s\nTest passed!\n\n", message);
        return ;
    }

    else if (err_code == expected_err_code && fabs(res - expected_res) < EPS) {
        printf("%s\nTest passed!\n\n", message);
        return ;
    }

    else {
        printf("expected result:           %lf\nresult by trapezium method:%lf\n", expected_res, res);
        printf("expected error code:%d\nerror code:         %d\n ", expected_err_code, err_code);
        printf("%s\n******TEST FAILED!******\n\n", message);
    }
}

double f1(double x) {
    return x;
}

double f2(double x) {
    return x*x;
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
    test(f1, 10., -10., -1, WRONG_SEGMENT, "Плохой отрезок");
    test(f1, 3., 10., 45.5, OK_RES, "Прямая");
    test(f4, -2. * pi, 10 * pi, 0., OK_RES, "cos"); 
    test(f5, pi, 2 * pi, -2., OK_RES, "sin");
    test(f6, 1., 10., 22023.747513, OK_RES, "exp");
    test(f2, -1e+2, 1e+5, 333333333666667., LACK_OF_ACCURACY, "Большой отрезок");
    test(f9, 1. + 1e-5, 1. + 1e-3, 0.0009895, OK_RES, "Маленький отрезок");
    test(f3, -1e+5, 1e+6, 249976001000495e+9, LACK_OF_ACCURACY, "GIANT SEGMENT");
}
