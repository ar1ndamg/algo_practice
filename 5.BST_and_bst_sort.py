"""
Invariant of BST is: for all nodes x, if y is in left subtree then key(y) < key(x)
                     if y is in right subtree key(y) >= key(x)

"""


class Node:
    key = None
    parent = None
    left_child = None
    right_child = None

    def __init__(self, key: int, parent=None, left_child=None, right_child=None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


def insert(root: Node, key: int):
    new_node = Node(key, root, None, None)
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
    if key < root.key:
        root.left_child = new_node
    else:
        root.right_child = new_node
    return head


def find_key(root: Node, key: int) -> (Node):
    """
    Finds the node having the key "key" and returns the reference of the node.
    If the key is not found then None is returned.
    """

    if not root:
        return None
    if key == root.key:
        return root
    elif key < root.key:
        return find_key(root.left_child, key)
    else:
        return find_key(root.right_child, key)


def delete_key(root: Node, key: int) ->(Node, Node):
    to_be_deleted = find_key(root, key)
    if to_be_deleted:
        new_child = to_be_deleted.left_child
        min_child = find_min(to_be_deleted.right_child)
        if min_child:
            print(min_child.key)
            min_child.left_child = to_be_deleted.left_child
            min_child.parent = to_be_deleted.parent
            if not min_child.right_child:
                min_child.right_child = to_be_deleted.right_child
                min_child.parent.left_child = None
            new_child = min_child
        if to_be_deleted is not root:
            if to_be_deleted is to_be_deleted.parent.left_child:
                to_be_deleted.parent.left_child = new_child
            else:
                to_be_deleted.parent.right_child = new_child
        else:
            root = new_child
        # to_be_deleted.parent=to_be_deleted.left_child=to_be_deleted.right_child = None
        return root,to_be_deleted
    else:
        return root, None


def find_min(root: Node) -> (Node):
    if not root:
        return None
    elif root.left_child:
        while root.left_child:
            root = root.left_child
        return root
    # elif root.right_child and root.right_child.left_child:
    #     return find_min(root.right_child)
    else:
        return root


def travarse_bst_preorder(root: Node):
    if not root:
        return
    print(root.key, end=',')
    travarse_bst_preorder(root.left_child)
    travarse_bst_preorder(root.right_child)


def travarse_bst_inorder(root: Node):
    if not root:
        return
    travarse_bst_inorder(root.left_child)
    print(root.key, end=',')
    travarse_bst_inorder(root.right_child)


if __name__ == "__main__":
    root = None
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 10)
    root = insert(root, 3)
    root = insert(root, 4)
    print("Preorder: ")
    travarse_bst_preorder(root)
    print("\b")
    print("Inorder: ")
    travarse_bst_inorder(root)
    print("\b")
    key = find_key(root, 5)
    root, deleted_node = delete_key(root, 8)
    #travarse_bst_preorder(root)
