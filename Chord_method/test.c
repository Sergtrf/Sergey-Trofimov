#include <stdio.h>
#include <math.h>
#include "chord_method.h"
#define EPS 1e-6
#define pi 3.141593

void test(rr_func f, double a, double b, double expected_res) {
    double res;
    double root_presence = chord_method(f, a, b, EPS, &res);

    if (root_presence == WRONG_SEGMENT && expected_res == WRONG_SEGMENT) {
	printf("Test passed!\n");
        return ;
    }
    
    if (fabs(expected_res - res) < EPS && root_presence == OK_ROOT) {
	printf("Test passed!\n");
	return ;
    }
    
    if (expected_res == NO_ROOT && root_presence == NO_ROOT) {
	printf("Test passed!\n");
	return ;
    }

    else {
        printf("expected result:       %lf\nresult by chord method:%lf\n", expected_res, res);
//	printf("ROOT PRESENCE: %lf\n", root_presence);
	printf("******TEST FAILED!******\n");
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
    test(f1, -1.0, 1.0, 0.0);
    test(f1, 100.0, 1.0, WRONG_SEGMENT);
    test(f1, -1e-5, 1e-3, 0.0);
    test(f1, -1e-7, 1e-7, 0.0);
    test(f2, 1.0, 3.0, 2.0);
    test(f3, -4.0, -2.0, -2.414214);
    test(f4, -3.0, 0.0, -pi/2.0);
    test(f4, 0.0, 0.0, WRONG_SEGMENT);
    test(f5, 1.0, 4.0, pi);
    test(f6, 2.0, 3.0, NO_ROOT);
    test(f7, -50.0, 20.0, -10.0);
    test(f8, -1.5, 0.0, NO_ROOT);
    test(f8, -1e+6, 1e+7, NO_ROOT);
    test(f9, 1e-4, 1e+8, 1.0);
    
    return 0;
}
