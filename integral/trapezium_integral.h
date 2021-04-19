typedef double (*rr_func)(double x);
#define OK_RES 1
#define LACK_OF_ACCURACY 0
#define WRONG_SEGMENT -1
#define IT_AMOUNT 1e+6

/*
Функция вычисляет интеграл данной f(x) на заданном отрезке [a;b] с заданной точностью epsilon.
Функция возвращает OK_RES, если нет помех для вычисления интеграла методом трапеций с N отрезками.
Функция возвращает WRONG_SEGMENT, если отрезок задан неверно.
*/
double integral(rr_func f, double a, double b, double eps, int *err_code);
