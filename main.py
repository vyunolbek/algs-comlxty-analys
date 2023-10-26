import structures.dheap as dh
from random import randint
from structures.k_mergesort import KMergeSort

dheap = dh.DHeap(10)
arr = [12, 12, 13, 5, 6, 7]

sorted_arr = dheap.heap_sort(arr)
arr = [12, 11, 13, 5, 6, 7, 1, 3, 8, 2, 9, 4]
print(sorted_arr)

arr = [randint(0, 100) for i in range(10)]

k_mergesort = KMergeSort(4)

print(k_mergesort.k_merge_sort(arr))