import sys
from math import *

def insertion_sort(elements):
    count = 0
    for i in range(len(elements)):
        j = 0
        tmp = elements[i]
        while (j < i):
            count += 1
            if (tmp < elements[j]):
                break
            j += 1
        elements.insert(j, tmp)
        del elements[i + 1]
    return (count)

