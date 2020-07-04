class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert_right(self,val):
        self.right = TreeNode(val)
    def insert_left(self,val):
        self.left = TreeNode(val)

def build_tree():
    mytree = TreeNode('10')
    mytree.insert_right('19')
    mytree.insert_left('5')
    mytree.left.insert_left('1')
    mytree.left.insert_right('6')
    mytree.right.insert_right('17')
    mytree.right.insert_left('21')
    return mytree

str1=''
str2=''
str3=''
def inorder(mytree):
    if mytree == None:
        return
    inorder(mytree.left)
    global str1
    str1+=" "+mytree.val
    inorder(mytree.right)

def preorder(mytree):
    if mytree == None:
        return
    global str2
    str2+=" "+mytree.val
    preorder(mytree.left)
    preorder(mytree.right)

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
preorder(mytree)
postorder(mytree)
print('inorder :',str1)
print('preorder :',str2)
print('postorder :',str3)


