import structures.dheap as dh

dheap = dh.DHeap(10)
arr = [12, 12, 13, 5, 6, 7]

sorted_arr = dheap.heap_sort(arr)
arr = [12, 11, 13, 5, 6, 7, 1, 3, 8, 2, 9, 4]
sorted_list = dheap.merge_sort(arr, 0, len(arr) - 1)
print(sorted_list)