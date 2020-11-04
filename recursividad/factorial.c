#include <stdio.h>

long result;
int n;

long factorial(int n)
{
  if (n == 0)
    return 1;
  else
    return (n * factorial(n - 1));
}

int main(int argc, char const *argv[])
{
  printf("Ingrese un número\n");
  scanf("%d", &n);
  if (n < 0)
    printf("el número no puede ser negativo");
  else
  {
    result = factorial(n);
    printf("%d! = %ld\n", n, result);
  }
  return 0;
}
