
class Node:
    key = None
    parent = None
    left_child = None
    right_child = None
    left_subtree_height = -1
    right_subtree_height = -1
    imbalanced_on = 'L'
    def __init__(self, key: int, parent: Node=None, left_child: Node=None, right_child: Node=None):
        self.key = key
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


def insert(root: Node, key: int):
    new_node = Node(key,root)
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
        root.left_subtree_height+=1
    else:
        root.right_child = new_node
        root.right_subtree_height+=1

    return head

def check_imbalance(node:Node):
    if abs(node.left_subtree_height-node.right_subtree_height) > 1:
        if node.left_subtree_height > 1:
            node.imbalanced_on = 'L'
        else:
            node.imbalanced_on = 'R'
    

def travarse_avl_tree_preorder(root: Node):
    if not root:
        return
    print(root.key, end=',')
    travarse_avl_tree_preorder(root.left_child)
    travarse_avl_tree_preorder(root.right_child)


def travarse_avl_tree_inorder(root: Node):
    if not root:
        return
    travarse_avl_tree_inorder(root.left_child)
    print(root.key, end=',')
    travarse_avl_tree_inorder(root.right_child)


if __name__ == "__main__":
    root = None
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 10)
    root = insert(root, 3)
    root = insert(root, 4)
    print("Preorder: ")
    travarse_avl_tree_preorder(root)
    print("\b")
    print("Inorder: ")
    travarse_avl_tree_inorder(root)
