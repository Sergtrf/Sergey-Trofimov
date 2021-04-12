typedef double (*rr_func)(double x);
#define OK_RES 1
#define LACK_OF_ACCURACY 0
#define WRONG_SEGMENT -1
#define ANOTHER_ERROR -1
#define MAX_IT 1e+6

double uniform_mesh_crushing(rr_func f, double a, double b, double eps, int *err_code);
