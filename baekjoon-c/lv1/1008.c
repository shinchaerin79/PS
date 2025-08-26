#include <stdio.h>

int main(void) {
  double A, B;
  scanf("%lf %lf", &A, &B);
  printf("%.12lf", A / B);
  return 0;
}