comparisons = 0

# def partition(array, low, high):
#     global comparisons
#     i = high + 1
#     pivot = array[low]

#     for j in range(high, low, -1):
#         comparisons += 1
#         if pivot <= array[j]:
#             i = i - 1
#             array[i], array[j] = array[j], array[i]
#     array[i - 1], array[low] = array[low], array[i - 1]
#     return (i - 1)

# def quick_sort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quick_sort(array, low, pi - 1)
#         quick_sort(array, pi + 1, high)
#     return (comparisons)

def partition(array, L, R):
    global comparisons
    pivot = array[0]

    for j in array[1:]:
        comparisons += 1
        if j < pivot:
            L.append(j)
        else:
            R.append(j)

def quick_sort(array):
    if len(array) > 1:
        L = []
        R = []
        partition(array, L, R)
        quick_sort(L)
        quick_sort(R)
    return (comparisons)