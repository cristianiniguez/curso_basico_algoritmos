// Para crear una Queue debemos seguir los siguientes pasos:

// Crear un pointer para saber que hay en front y rear
// Colocar estos valores en -1 al inicializar
// Incrementar en 1 el valor de “rear” cuando agregamos un elemento
// Retornar el valor de front al quitar un elemento e incrementar en 1 el valor de front a usar dequeue.
// Antes de agregar un elemento revisar si hay espacios
// Antes de remover un elemento revisamos que existan elementos
// Asegurarnos de que al remover todos los elementos resetear nuestro front y rear a -1 y agregar el valor de 0 a Front al hacer nuestro primer enqueue

#include <stdio.h>
#define SIZE 5

int values[SIZE], front = -1, rear = -1;

void enQueue(int value)
{
  if (rear == SIZE - 1)
    printf("Nuestro queue está lleno\n");
  else
  {
    if (front == -1)
      front = 0;
    rear++;
    values[rear] = value;
    printf("Se insertó el valor %d correctamente\n", value);
  }
}

void deQueue()
{
  if (front == -1)
    printf("Nuestro queue está vacío\n");
  else
  {
    printf("Se eliminó el valor %d\n", values[front]);
    front++;
    if (front > rear)
      front = rear = -1;
  }
}

int main(int argc, char const *argv[])
{
  enQueue(1); // Se insertó el valor 1 correctamente
  enQueue(2); // Se insertó el valor 2 correctamente
  enQueue(3); // Se insertó el valor 3 correctamente
  enQueue(4); // Se insertó el valor 4 correctamente
  enQueue(5); // Se insertó el valor 5 correctamente
  deQueue();  // Se eliminó el valor 1
  deQueue();  // Se eliminó el valor 2
  deQueue();  // Se eliminó el valor 3
  deQueue();  // Se eliminó el valor 4
  deQueue();  // Se eliminó el valor 5
  enQueue(6); // Se insertó el valor 6 correctamente
  return 0;
}
