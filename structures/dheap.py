class DHeap:
    def __init__(self, d):
        self.d = d
        self.heap_list = []

    def insert(self, x):
        self.heap_list.append(x)
        self.bubble_up(len(self.heap_list)-1)

    def bubble_up(self, i):
        if i == 0:
            return
        p = (i-1)//self.d
        if self.heap_list[i] > self.heap_list[p]:
            self.heap_list[i], self.heap_list[p] = self.heap_list[p], self.heap_list[i]
            self.bubble_up(p)

    def extract_max(self):
        if not self.heap_list:
            return None  
        if len(self.heap_list) == 1:
            return self.heap_list.pop() 
        root = self.heap_list[0] 
        self.heap_list[0] = self.heap_list.pop() 
        self.bubble_down(0)  
        return root 

    def bubble_down(self, i):
        children = [self.d*i + j for j in range(1, self.d+1)]
        max_child = max(children, key=lambda x: self.heap_list[x] if x < len(self.heap_list) else float('-inf'))
        if max_child < len(self.heap_list) and self.heap_list[max_child] > self.heap_list[i]:
            self.heap_list[i], self.heap_list[max_child] = self.heap_list[max_child], self.heap_list[i]
            self.bubble_down(max_child)

    def max_child(self, index):
        start = self.D * index + 1
        end = min(len(self.heap_list), start + self.D)
        if start > len(self.heap_list):
            return None
        return max(range(start, end), key=lambda x: self.heap_list[x], default=None)
    
    def heap_sort(self, arr):
        for element in arr:
            self.insert(element)

        sorted_arr = []
        while True:
            max_element = self.extract_max()
            if max_element is not None:
                sorted_arr.append(max_element)
            else:
                break
        return sorted_arr
    
    def merge(self, arr, left, middle1, middle2, middle3, right):
    # Реализация слияния четырех упорядоченных подсписков

        # Создайте четыре D-кучи
        d_heap1 = DHeap(4)
        d_heap2 = DHeap(4)
        d_heap3 = DHeap(4)
        d_heap4 = DHeap(4)

        print(left, middle1, middle2, middle3, right)

        for i in range(left, middle1 + 1):
            d_heap1.insert(arr[i])

        for i in range(middle1 + 1, middle2 + 1):
            d_heap2.insert(arr[i])

        for i in range(middle2 + 1, middle3 + 2):
            print(arr[i])
            d_heap3.insert(arr[i])

        for i in range(middle3 + 1, right + 1):
            d_heap4.insert(arr[i])

        # Объединяем подсписки в один отсортированный список
        i = left
        while True:
            print(d_heap1.heap_list, d_heap2.heap_list, d_heap3.heap_list, d_heap4.heap_list)
            min_heap = min(d_heap1, d_heap2, d_heap3, d_heap4, key=lambda h: h.heap_list[0])
            if not min_heap.heap_list:
                break
            arr[i] = min_heap.extract_max()
            i += 1

    def merge_sort(self, arr, left, right):
        if left < right:
            middle1 = left + (right - left) // 4
            middle2 = left + 2 * (right - left) // 4
            middle3 = left + 3 * (right - left) // 4

            self.merge_sort(arr, left, middle1)
            self.merge_sort(arr, middle1 + 1, middle2)
            self.merge_sort(arr, middle2 + 1, middle3)
            self.merge_sort(arr, middle3 + 1, right)

            self.merge(arr, left, middle1, middle2, middle3, right)