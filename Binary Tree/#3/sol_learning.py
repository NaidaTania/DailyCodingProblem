class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Codec:
    def serialize(self, root):
        def _post_order(node):
            if not node:
                return '', 0
            left_str, left_size = _post_order(node.left)
            print("left str: {} left size: {}".format(left_str,left_size))
            right_str, right_size = _post_order(node.right)
            print("right str: {} right size: {}".format(right_str,right_size))
            string = '{}_{}_{}'.format(node.val, left_size, right_size)
            print("                            ", string)
            if left_size:
                string += ',' + left_str
            if right_size:
                string += ',' + right_str
            return string, left_size + right_size + 1
        return _post_order(root)[0]

    def deserialize(self, data):
        nodes = data.split(',')
        def _rec(nodes, i):
            node = nodes[i]
            if not node:
                return None
            val, left_size, right_size = node.split('_')
            val, left_size, right_size = int(val), int(left_size), int(right_size)
            root = TreeNode(val)
            root.left = _rec(nodes, i + 1) if left_size > 0 else None
            root.right = _rec(nodes, i + left_size + 1) if right_size > 0 else None
            return root
        return _rec(nodes, 0)
# def deserialize(s):





node = Node('root', Node('left', Node('left.left')), Node('right'))
s = Codec()
print(s.serialize(node))

# assert deserialize(serialize(node)).left.left.val == 'left.left'