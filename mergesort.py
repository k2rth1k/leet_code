def merge_sort(arr):
    length = len(arr)
    if length == 1 or length == 0:
        return arr
    mid = (length // 2)
    left = arr[:mid]
    right = arr[mid:]
    left_arr = merge_sort(left)
    right_arr = merge_sort(right)
    return merge(left_arr, right_arr)



def merge(left_arr, right_arr):
    arr = []
    i = 0
    j = 0
    c = 0
    left_length = len(left_arr)
    right_length = len(right_arr)
    while i < left_length and j < right_length:
        if left_arr[i] < right_arr[j]:
            arr.append(left_arr[i])
            c += 1
            i += 1
        else:
            arr.append(right_arr[j])
            c += 1
            j += 1
    while i < left_length:
        arr.append( left_arr[i])
        c += 1
        i += 1
    while j < right_length:
        arr.append(right_arr[j])
        c += 1
        j += 1
    return arr


if __name__ == '__main__':
    print(merge_sort([5, 2, 3, 4, 1]))
