#include <math.h>
#include "chord_method.h"

double chord_method(rr_func f, double a, double b, double eps, double *res) {
    double f_a = f(a);
    double f_b = f(b);
    double x;
    double f_x;
    int amount_of_it = 0;

    if (a >= b) return WRONG_SEGMENT;

    if (f_a * f_b > 0) return WRONG_SEGMENT;

    do {
	x = (a * f_b - b * f_a) / (f_b - f_a);
        f_x = f(x);

        if (f_x * f_a > 0) {
	    f_a = f_x;
	    a = x;
    	}

	else {
	    f_b = f_x;
	    b = x;
	}

        amount_of_it++;
    } while (fabs(f_x) >= eps && fabs(a - b) >= eps && amount_of_it < MAX_IT);

    if (amount_of_it >= MAX_IT || f_x >= eps || x < a || x > b) return NO_ROOT;
    
    *res = x;
    return OK_ROOT;
}
