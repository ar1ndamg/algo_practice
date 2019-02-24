""" 
    Heap is an Array that can be visualized as nearly complete binary tree. 
    left child is at i*2, right child at i*2+1, parent of i is at i/2.
    Assuming that the root of the tree is at index 1 of the array.
"""


def heap_sort(arr: list, size: int):
    biuld_max_heap(arr,size)
    """
        This function first builds a max heap from the unsorted array,
        and then extracts the first element from the max heap and keeps doing this untill 
        the heap is empty
    """
    sorted_arr = [None]*size
    for i in range(size):
        sorted_arr[i], size = extract_max(arr, size)
    return sorted_arr


def biuld_max_heap(arr: list, size: int):
    """ 
        Builds a max heap from an unordered array
        Elements in the heap Arr[n/2+1,..,n] will be leaves so we don't 
        need to heapify them.
    """
    for i in range(size//2, 0, -1):
        """ start from bottom last level and call max_heapify
            at each level upwards.
        """
        max_heapify(arr, i, size)
    return arr


def max_heapify(arr: list, root: int, size: int):
    """ 
        Correct a single violation of the max heap property in a subtree's root. 
        It assumes that left subtree and right subtree of the root are already max heaps 
    """
    has_left_child = True
    has_right_child = True
    left_child = root*2
    right_child = root*2+1
    max_child_index = root

    if left_child > size:
        has_left_child = False
    if right_child > size:
        has_right_child = False

    if (has_left_child and has_right_child and arr[left_child] > arr[right_child]) or (has_left_child and not has_right_child):
        max_child_index = left_child
    elif has_right_child and arr[left_child] < arr[right_child]:
        max_child_index = right_child

    if max_child_index != root and arr[max_child_index] > arr[root]:
        # swap the root element with max_child_index element
        arr[root], arr[max_child_index] = arr[max_child_index], arr[root]
        max_heapify(arr, max_child_index, size)


def extract_max(arr: list, size: int):
    """
    This function extracts the maximum element i.e, the first element.
    after getting the top, it swaps first and last element in the heap ,reduces the
    size of the heap by 1, hence discarding the maximum element.
    """
    top = arr[1]
    # swap the first element with the last element and discard the last element
    arr[1], arr[size] = arr[size], arr[1]
    size -= 1
    max_heapify(arr, 1, size)
    return top, size


if __name__ == "__main__":
    arr = [-1, 5, 3, 4, 1, 6, 8, 11, 25, 54, 32, 21, 12]
    print(biuld_max_heap(arr, len(arr)-1))
    print(heap_sort(arr, len(arr)-1))
    print(arr)
