# include <stdio.h>
# include <math.h>

double hypotenuse( int a, int b);
int main()
{
    int a, b;
    double c;

    int maximum_c = 50;
    double epsilon = 1e-3;

    for (a = 1; a < maximum_c; a++) {
        for (b = a; b < maximum_c; b++) {
            c = hypotenuse(a, b);
            if ( (c <= (double)(maximum_c) ) &&
                 (c - floor(c) < epsilon ) ) {
               printf("%4d%4d%4d\n", a, b, (int)c);
            }
        }
    }
    return 0;
}
