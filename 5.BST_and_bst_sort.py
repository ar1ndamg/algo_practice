"""
Invariant of BST is: for all nodes x, if y is in left subtree then key(y) < key(x)
                     if y is in right subtree key(y) >= key(x)

"""
class Node:
    key = None
    parent = None
    left_child = None
    right_child = None
    def __init__(self,key: int, parent, left_child, right_child):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


def insert(root:Node, key: int):
    new_node = Node(key,root,None,None)
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

def travarse_bst_preorder(root:Node):
    if not root:
        return
    print(root.key,end=',')
    travarse_bst_preorder(root.left_child)
    travarse_bst_preorder(root.right_child)

def travarse_bst_inorder(root:Node):
    if not root:
        return
    travarse_bst_inorder(root.left_child)
    print(root.key,end=',')
    travarse_bst_inorder(root.right_child)

if __name__ == "__main__":
    root = None
    root = insert(root,5)
    root = insert(root,8)
    root = insert(root, 10)
    root = insert(root, 3)
    root = insert(root, 4)
    print("Preorder: ")
    travarse_bst_preorder(root)
    print("\b")
    print("Inorder: ")
    travarse_bst_inorder(root)