array = [
    3, 94, 86, 82, 90,
    10, 87, 36, 61, 8,
    17, 15, 22, 10, 23,
    78, 25, 2, 30, 45,
    98, 43, 98, 59, 53,
    57, 2, 64, 1, 41,
    32, 58, 19, 99, 60,
    74, 48, 80, 44, 25,
    68, 1, 89, 77, 60,
    25, 99, 30, 76, 32,
    57, 82, 52, 44, 72,
    87, 34, 87, 65, 30,
    54, 6, 31, 33, 44,
    44, 42, 82, 90, 17,
    9, 98, 28, 86, 69,
    3, 17, 8, 45, 98,
    12, 47, 95, 43, 72,
    39, 41, 82, 74, 56,
    65, 79, 50, 26, 67,
    100, 24, 67, 38, 57
]


def merge(array1, array2):
    merged_array = []
    i1 = 0
    i2 = 0
    while i1 < len(array1) and i2 < len(array2):
        if array1[i1] < array2[i2]:
            merged_array.append(array1[i1])
            if i1 == len(array1) - 1:
                for x2 in array2[i2:]:
                    merged_array.append(x2)
                return merged_array
            i1 += 1
        else:
            merged_array.append(array2[i2])
            if i2 == len(array2) - 1:
                for x1 in array1[i1:]:
                    merged_array.append(x1)
                return merged_array
            i2 += 1


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        m = int(len(array) / 2)
        array1 = array[:m]
        array2 = array[m:]
        sorted_array1 = merge_sort(array1)
        sorted_array2 = merge_sort(array2)
        return merge(sorted_array1, sorted_array2)


print(array)
sorted_array = merge_sort(array)
print(sorted_array)
