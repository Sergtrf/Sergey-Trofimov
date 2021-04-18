#include <math.h>
#include "uniform_mesh_crushing.h"

static double next_segment_search(rr_func f, double eps, double a, double b, double *a0, double *b0, double *x0) {
    double f_b = (*f)(b);
    double step = (b - a) / 100.0;
    double x1 = a;
    double x3 = x1 + step;
    double x2 = (x3 + x1) / 2.0;
    double f_x1 = (*f)(x1);
    double f_x2 = (*f)(x2);
    double f_x3 = (*f)(x3);
    double f_min = f_x2;
    
    do {
	if (((f_x2 <= f_x1) || (f_x2 <= f_x3)) && (f_x2 < f_min)) {
	    *a0 = x1;
            *b0 = x3;
	    *x0 = x2;
	    f_min = f_x2;
	}
        x1 += step;
	x2 += step;
	x3 += step;
	f_x1 = (*f)(x1);
        f_x2 = (*f)(x2);
	f_x3 = (*f)(x3);
    } while (fabs(x3 - b) >= eps);
    return f_min;
}

double uniform_mesh_crushing(rr_func f, double a, double b, double eps, int *err_code) {
    double f_a = (*f)(a);
    double f_b = (*f)(b);
    double x;
    double f_x;
    double res = f_x;
    int amount_of_it = 0;

    if (a >= b){
	*err_code = WRONG_SEGMENT;
	return -1;
    }

    do {
	f_x = next_segment_search(f, eps, a, b, &a, &b, &x);
	amount_of_it += 100;
	f_a = (*f)(a);
	f_b = (*f)(b);
	
    } while (fabs(a - b) >= eps && amount_of_it < MAX_IT); 
    
    res = f_x;

    if (amount_of_it >= MAX_IT) {
	*err_code = LACK_OF_ACCURACY;
	return res;
    }

    if (fabs(a - b) < eps && f_x < f_a && f_x < f_b) {
	*err_code = OK_RES;
	return res;
    }
    
    else {
	*err_code = ANOTHER_ERROR;
	return res;
    }
}
