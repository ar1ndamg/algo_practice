"""
    There is only one runway in the airport. So only one plane can
    use the runway at a single time. Our task is to schedule the timings
    of the flights, each flight require k minutes of the runway. To do that the steps required are:
    1. Find the insertion point i where a[i]>=t+k>=a[i-1] (t is the timing of the 
       flight to be scheduled)
    2. Compare a[i] and a[i-1] against t and see if it can be scheduled
    3. Insert t into the schedule i.e, insert into the array a

    * we cannot use unsorted array as finding the insertion point will take O(n)
      time, same for heaps
    * if we use a sorted array we can find the insertion point in O(lg(n)) time,
      but to insert t in the array, shifting will be required which takes O(n) time
    ** We can use Binary Search Trees as step 2 and step 3 can be done in O(lg(n)) time
"""
"""
Invariant of BST is: for all nodes x, if y is in left subtree then key(y) < key(x)
                     if y is in right subtree key(y) >= key(x)

"""


class Node:
    def __init__(self, key: int, parent=None, left_child=None, right_child=None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.subtree_size = 1


def insert(root: Node, key: int):
    """
    Insert a new flight time to the schedule
    """
    print(f"Inserting {key}")
    inserted = False
    new_node = Node(key, root)
    head = root
    if not root:
        root = new_node
        return root
    while root:
        if key < root.key and root.left_child:
            root = root.left_child
        elif key >= root.key and root.right_child:
            root = root.right_child
        else:
            break
    new_node.parent = root
    # check if k minute window is available
    if abs(root.key - key) >= 3:
        if key < root.key:
            root.left_child = new_node
        else:
            root.right_child = new_node
        inserted = True
        add_to_parent_subtree_size(root)
    if inserted:
        print(f"{key} inserted successfully.")
    else:
        print(f"{key} can not be added")
    return head


def add_to_parent_subtree_size(root: None):
    """ 
    Recursively calls its parent to increase the subtree size by 1
    """
    if not root:
        return
    root.subtree_size += 1
    add_to_parent_subtree_size(root.parent)


def flights_before_t(root: Node, t: int):
    """
    returns the number of flights that are scheduled before 't'
    """
    count = 0
    while root and root.key <= t:
        if root.key <= t:
            count += root.left_child.subtree_size
            count += 1
            root = root.right_child
        else:
            root = root.left_child
    return count


def traverse_bst_preorder(root: Node):
    """
    Preorder traversal of the BST
    """
    if not root:
        return
    print(f"key: {root.key} subtree size: {root.subtree_size}", end=',')
    traverse_bst_preorder(root.left_child)
    traverse_bst_preorder(root.right_child)


def traverse_bst_inorder(root: Node):
    """
    Inorder traversal of the BST
    """
    if not root:
        return
    traverse_bst_inorder(root.left_child)
    print(root.key, end=',')
    traverse_bst_inorder(root.right_child)


if __name__ == "__main__":
    root = None
    arr = [5, 3, 4, 1, 15, 8, 11, 25, 54, 32, 21, 12]
    for i in arr:
        root = insert(root, i)
    print("Preorder: ")
    traverse_bst_preorder(root)
    print("")
    print("Inorder: ")
    traverse_bst_inorder(root)
    print("")
    c = flights_before_t(root, 25)
    print(c)