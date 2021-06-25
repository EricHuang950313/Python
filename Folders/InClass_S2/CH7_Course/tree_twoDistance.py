class treeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertLeft(self, val):
        if self.left == None:
            self.left = treeNode(val)
        else:
            self.left.insertLeft(val)

    def insertRight(self, val):
        if self.right == None:
            self.right = treeNode(val)
        else:
            self.right.insertRight(val)


def tree_height(tree):
    if tree.left == None and tree.right == None:
        return 1
    else:
        if tree.left == None:
            return tree_height(tree.right) + 1
        elif tree.right == None:
            return tree_height(tree.left) + 1
        else:
            return max(tree_height(tree.right), tree_height(tree.left)) + 1


def myprint_node(tree, lvl):
    if tree == None:
        pass
    elif lvl == 1:
        print(tree.val)
    elif lvl > 1:
        myprint_node(tree.left, lvl - 1)
        myprint_node(tree.right, lvl - 1)


def kDistance(tree, k):
    if k == 0:
        print(tree.val)
    else:
        if tree.left != None:
            kDistance(tree.left, k - 1)
        if tree.right != None:
            kDistance(tree.right, k - 1)


def buildTree():
    tree = treeNode('A')
    tree.insertLeft('B')
    tree.insertRight('C')
    tree.right.insertRight('F')
    tree.left.insertLeft('D')
    tree.left.insertRight('E')
    tree.left.right.insertLeft('G')
    tree.left.right.insertRight('H')
    return tree


def LCA(root, n1, n2):
    if root is None:
        return None
    if root.val == n1 or root.val == n2:
        return root
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)
    if left is not None and right is not None:
        return root
    if left:
        return left
    else:
        return right


def findLevel(root, data, d, level):
    if root is None:
        return
    if root.val == data:
        d.append(level)
        return
    findLevel(root.left, data, d, level + 1)
    findLevel(root.right, data, d, level + 1)


def findDistance(root, n1, n2):
    lca = LCA(root, n1, n2)
    d1 = []
    d2 = []
    if lca:
        findLevel(lca, n1, d1, 0)
        findLevel(lca, n2, d2, 0)
        return d1[0] + d2[0]
    else:
        return -1


tree_root = buildTree()
kDistance(tree_root, 1)
print(findDistance(tree_root, 'D', 'H'))