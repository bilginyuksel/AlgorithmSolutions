from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_left_view_of_binary_tree(tree):
    node = tree
    queue = deque([[node, 0]])

    level_order = defaultdict(TreeNode)

    while queue and len(queue) > 0:
        node, curr_level = queue.popleft()
        if curr_level not in level_order:
            level_order[curr_level] = node
        
        if node.left is not None:
            queue.append([node.left, curr_level +1])
        if node.right is not None:
            queue.append([node.right,curr_level + 1])

    result = [] 
    for level, node in level_order.items():
        result.append(node.value)

    return result

def create_sample_tree():
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(9)
    tree.left.left = TreeNode(12) 
    tree.left.right = TreeNode(15)
    tree.left.right.right = TreeNode(22)
    tree.left.right.right.left = TreeNode(30)

    return tree

root = create_sample_tree()
res = get_left_view_of_binary_tree(root)
print(res)


