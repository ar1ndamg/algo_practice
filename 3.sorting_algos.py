def insertion_sort(arr: list):
    """ Takes an list and sorts it using insertion sort algorithm """
    l = len(arr)
    #print(f"length: {l}")
    for i in range(1, l):
        key = arr[i]
        j = i-1
        while j >= 0:
            if key < arr[j]:
                # slide the elements what are greater than the key to the right in the sorted array
                swap(arr, j, j+1)
            j -= 1
    return arr


def swap(arr, i, j):
    #print(f"swapping: {arr[i]},{arr[j]}")
    arr[i], arr[j] = arr[j], arr[i]


def merge_sort(arr: list, start: int, end: int):
    """ Takes an list and sorts it using merge sort algorithm """
    if end == start:
        return [arr[start]]
    else:
        mid = start + (end - start)//2
        left = merge_sort(arr, start, mid)
        right = merge_sort(arr, mid+1, end)
        sorted_arr = merge(left, right)
        return sorted_arr


def merge(left: list, right: list):
    i = j = k = 0
    l1 = len(left)
    l2 = len(right)
    arr = [0]*(l1+l2)
    while k < l1+l2 and i < l1 and j < l2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while(i < l1):
        arr[k] = left[i]
        i += 1
        k += 1
    while(j < l2):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


if __name__ == '__main__':
    arr = [5, 3, 4, 1, 6, 8, 11, 25, 54, 32, 21, 12]
    print(merge_sort(arr, 0, len(arr)-1))
    print(insertion_sort(arr))
