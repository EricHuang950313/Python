class TreeNode():
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left
    def insert_right(self, val):
        self.right = TreeNode(val)
    def insert_left(self, val):
        self.left = TreeNode(val)

def build_tree():
    mytree = TreeNode("A")
    mytree.insert_left("B")
    mytree.left.insert_left("D")
    mytree.left.insert_right("E")
    mytree.insert_right("C")
    mytree.right.insert_left("F")
    return mytree

str1 = ""
str3 = ""

def inorder(mytree):
    if mytree == None:
        return
    inorder(mytree.left)
    global str1
    str1+=" "+mytree.val
    inorder(mytree.right)

def postorder(mytree):
    if mytree == None:
        return
    global str3
    postorder(mytree.left)
    postorder(mytree.right)
    str3+=" "+mytree.val

mytree = build_tree()
print()
inorder(mytree)
postorder(mytree)
print('inorder :',str1)
print('postorder :',str3)
