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
    ### A tree
    mytree = TreeNode("A")
    mytree.insert_right("C")
    mytree.insert_left("B")
    ### B tree
    mytree.left.insert_left("D")
    mytree.left.insert_right("E")
    mytree.left.right.insert_right("H")
    mytree.left.right.insert_left("G")
    ### C tree
    mytree.right.insert_right("F")
    return mytree

def myheight(mytree):
    if mytree.right == None and mytree.left == None:
        return 1
    elif mytree.right == None :
        return myheight(mytree.left) + 1
    elif mytree.left == None :
        return myheight(mytree.right) + 1
    else:
        return max(myheight(mytree.right),myheight(mytree.left))+1

str1 = ""
str2 = ""
str3 = ""
str4 = ""
str5 = ""

def inorder(mytree):  #中序走訪:左中右
    if mytree == None:
        return
    inorder(mytree.left)
    global str1
    str1+=mytree.val
    #print(mytree.val)
    inorder(mytree.right)

def preorder(mytree): #前序走訪:中左右
    if mytree == None:
        return
    global str2
    str2+=mytree.val
    #print(mytree.val)
    preorder(mytree.left)
    preorder(mytree.right)

def postorder(mytree): #後序走訪:左右中
    if mytree == None:
        return
    global str3
    postorder(mytree.left)
    postorder(mytree.right)
    str3+=mytree.val
    #print(mytree.val)

def levelorder(mytree):
    H = myheight(mytree)
    for i in range(1, H+1):
        myprint_node(mytree, i)

def myprint_node(mytree, i):
    global str4
    if mytree == None:
        pass
    elif i == 1:
        str4 += mytree.val
        # print(mytree.val)
    elif i > 1:
        myprint_node(mytree.left, i - 1)
        myprint_node(mytree.right, i - 1)

def KDistance(mytree, k):
    global str5
    if k == 0:
        str5 += mytree.val
        #print(mytree.val)
    if k > 0:
        if mytree.left != None:
            KDistance(mytree.left, k-1)
        if mytree.right != None:
            KDistance(mytree.right, k-1)

def twoDistance(mytree, a, b):
    print()

def findDistance(mytree, i):
    pass

mytree = build_tree()
inorder(mytree)
preorder(mytree)
postorder(mytree)
levelorder(mytree)
KDistance(mytree, 2)
print("height :",myheight(mytree))
print("inorder :",str1)
print("preorder :",str2)
print("postorder :",str3)
print("levelorder :",str4)
print("distance<2> :",str5)