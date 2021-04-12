#include <stdio.h>
#include <math.h>
#include "chord_method.h"
#define EPS 1e-6
#define pi 3.141593

void test(rr_func f, double a, double b, double expected_res, int expected_err_code, char *message) {
    double res;
    int err_code;
    res = uniform_mesh_crushing(f, a, b, EPS, &err_code);

    if (err_code == expected_err_code || fabs(res - expected_res) < EPS) {
        printf("Test passed!\n%s\n", message);
        return ;
    }

    else {
        printf("expected result:                       %lf\nresult by uniform mesh crushing method:%lf\n", expected_res, res);
        printf("%s\n******TEST FAILED!******\n", message);
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
    return pow(x, 5) + 1e+5;
}

double f8(double x) {
    return cos(x) + 2;
}

double f9(double x) {
    return 1/x - 1;
}

int main() {

                                                              45,1          35%

