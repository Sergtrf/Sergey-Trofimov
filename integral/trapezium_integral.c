#include <math.h>
#include "trapezium_integral.h"

double integral(rr_func f, double a, double b, double eps, int *err_code) {
    if (a >= b) {
        *err_code = WRONG_SEGMENT;
	return -1;
    }
    
    double height = (b - a) / IT_AMOUNT;
    double x1 = a;
    double x2 = x1 + height;
    double f_x1 = (*f)(x1);
    double f_x2 = (*f)(x2);
    double area = height * (f_x1 + f_x2) / 2.;
    double res = area;

    for (int i = 0; i < IT_AMOUNT - 1; i++) {
	x1 += height;
	x2 += height;
	f_x1 = (*f)(x1);
	f_x2 = (*f)(x2);
	area = height * (f_x1 + f_x2) / 2.;
 	res += area;
    } 

    *err_code = OK_RES;
    return res;
}
