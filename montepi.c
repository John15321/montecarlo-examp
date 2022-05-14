#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int main(int argc, char** argv) {
    unsigned long iters, count = 0;
    double x, y, z, pi;
    clock_t tStart, tEnd;

    if(argc != 2) {
        printf("Enter the number of iterations used to estimate pi: ");
        scanf("%ld", &iters);
    } else iters = atol(argv[1]);
    srand(time(NULL));
    count = 0;
    tStart = clock();
    for (unsigned long i = 0; i < iters; ++i) {
      x = (double)rand() / RAND_MAX;
      y = (double)rand() / RAND_MAX;
      z = x * x + y * y;
      if (z <= 1) ++count;
    }
    pi = (double)count / iters * 4;
    tEnd = clock();
    printf("Number of iterations = %ld\n", iters);
    printf("Estimate of pi =  %.10lf\n", pi);
    printf("Estimate of pi error = %.10lg (%lg%%)\n", fabs(pi - M_PI), fabs(pi - M_PI) * 100 / M_PI);
    printf("Time taken = %lg milliseconds\n", (double)(tEnd - tStart) * 1000 / CLOCKS_PER_SEC);
    return 0;
}