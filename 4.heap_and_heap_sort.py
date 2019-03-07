""" 
    Heap is an Array that can be visualized as nearly complete binary tree. 
    left child is at i*2, right child at i*2+1, parent of i is at i/2.
    Assuming that the root of the tree is at index 1 of the array. 
    The first element of the array, i.e, a[0] contains the size of the heap.
"""


def heap_sort(arr: list, size: int = None) -> (list):
    """
        This function first builds a max heap from the unsorted array,
        and then extracts the first element from the max heap and keeps doing this untill 
        the heap is empty
    """
    build_max_heap(arr, arr[0])
    sorted_arr = [None]*arr[0]
    for i in range(arr[0]):
        sorted_arr[i], arr[0] = extract_max(arr, arr[0])
    return sorted_arr


def insert_to_heap(arr: list, val: int) -> (None):
    """
    Inserts a new element to the heap in O(lg(n)) time
    """
    arr.append(val)
    arr[0] += 1
    parent = arr[0]//2
    while(parent > 0):
        max_heapify(arr, parent)
        parent = parent//2

def delete_from_heap(arr: list,key: int) ->(int):
    """
    Deletes a key from the heap in O(n) time and returns the index 
    of that deleted element. If the element is not present in heap
    None is returned.
    """
    index = None
    for i in range(1,arr[0]+1):
        if arr[i] == key:
            index = i
            break
    if index:
        arr[index] = arr[arr[0]]
        arr[0]-=1
        max_heapify(arr, index) 
    else:
        return None

def build_max_heap(arr: list, size: int = None) -> (list):
    """ 
        Builds a max heap from an unordered array
        Elements in the heap Arr[n/2+1,..,n] will be leaves so we don't 
        need to heapify them.
    """
    for i in range(arr[0]//2, 0, -1):
        """ start from bottom last level and call max_heapify
            at each level upwards.
        """
        max_heapify(arr, i)
    return arr


def max_heapify(arr: list, root: int, size: int = None) -> (None):
    """ 
        Correct a single violation of the max heap property in a subtree's root. 
        It assumes that left subtree and right subtree of the root are already max heaps 
    """
    has_left_child = True
    has_right_child = True
    left_child = root*2
    right_child = root*2+1
    max_child_index = root

    if left_child > arr[0]:
        has_left_child = False
    if right_child > arr[0]:
        has_right_child = False

    if (has_left_child and has_right_child and arr[left_child] > arr[right_child]) or (has_left_child and not has_right_child):
        max_child_index = left_child
    elif has_right_child and arr[left_child] < arr[right_child]:
        max_child_index = right_child

    if max_child_index != root and arr[max_child_index] > arr[root]:
        # swap the root element with max_child_index element
        arr[root], arr[max_child_index] = arr[max_child_index], arr[root]
        max_heapify(arr, max_child_index)


def extract_max(arr: list, size: int = None) -> (int,int):
    """
    This function extracts the maximum element i.e, the first element.
    after getting the top, it swaps first and last element in the heap ,reduces the
    size of the heap by 1, hence discarding the maximum element.
    """
    top = arr[1]
    # swap the first element with the last element and discard the last element
    arr[1], arr[arr[0]] = arr[arr[0]], arr[1]
    arr[0] -= 1
    max_heapify(arr, 1)
    return top, arr[0]


if __name__ == "__main__":
    arr = [12, 5, 3, 4, 1, 6, 8, 11, 25, 54, 32, 21, 12]
    print(build_max_heap(arr))
    # print(heap_sort(arr))
    print(arr)
    insert_to_heap(arr, 45)
    insert_to_heap(arr, 68)
    print(arr)
