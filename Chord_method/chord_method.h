typedef double (*rr_func)(double x);
#define NO_ROOT -1
#define OK_ROOT 0 
#define WRONG_SEGMENT -1
#define MAX_IT 1e+6

/*
Функция вычисляет корень уравнения f(x) = 0 (f заданная функция) на заданном отрезке [a;b] с заданной точность epsilon.
Функция возвращает NO_ROOT в случае, если корня на данном отрезке нет,
возвращает OK_ROOT, если корень есть.
Если отрeзок [a;b] не корректен, то функция возвращает WRONG_SEGMENT.
Если корень есть, то переменной res присваивается значение корня.
*/
double chord_method(rr_func f, double a, double b, double eps, double *res);
