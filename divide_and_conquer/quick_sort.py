# necesitamos dividir nuestro dataset
# necesitamos un punto pivotal
# recursivamente ordenar cada mitad de mi array

import random


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)  # Ordenando los datos mas chicos
        quickSort(arr, pi + 1, high)  # Ordenando los datos más grandes


arr = []

for i in range(10):
    arr.append(random.randint(1, 100))

print('Before:', arr)

quickSort(arr, 0, len(arr) - 1)

print('After:', arr)
