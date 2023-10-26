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