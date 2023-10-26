def k_merge_sort(arr, k):
    if len(arr) <= 1:
        return arr
    else:
        n = len(arr)
        chunk_size = n // k if n // k > 0 else 1
        chunks = [arr[i:i+chunk_size] for i in range(0, n, chunk_size)]
        sorted_chunks = [k_merge_sort(chunk, k) for chunk in chunks]
        return merge(sorted_chunks)

def merge(sorted_chunks):
    if len(sorted_chunks) == 1:
        return sorted_chunks[0]
    else:
        mid = len(sorted_chunks) // 2
        left = merge(sorted_chunks[:mid])
        right = merge(sorted_chunks[mid:])
        return merge_two_lists(left, right)

def merge_two_lists(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

a = []