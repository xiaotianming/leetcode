class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def CreatTree(list_tree):
    if len(list_tree) < 1 :
        return None
    root = TreeNode(list_tree[0])
    node_list = []
    node_list.append(root)
    if len(list_tree) < 2:
        return root
    i = 1
    while i < len(list_tree):
        node = node_list.pop(0)
        node.left = TreeNode(list_tree[i])
        node_list.append(node.left)
        i += 1
        if i < len(list_tree):
            node.right = TreeNode(list_tree[i])
            node_list.append(node.right)
            i += 1
    return root


def PrintTree(root):
    if root is None:
        return None
    print(root.val)
    PrintTree(root.left)
    PrintTree(root.right)


if __name__ == '__main__':
    s = [5, 4, 5, 1, 1, 5]
    tree = CreatTree(s)
    PrintTree(tree)

