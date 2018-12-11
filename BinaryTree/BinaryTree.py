class BinaryTree:
    def __init__(self, data = None, leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

    def isEmpty(self):
        return self.data == None

    def __str__(self):
        '''This function does an in-order traversal'''

        if(self.isEmpty()):
            return "Empty"

        else:
            result = " "
            if(self.getLeftChild() != None):
                result += BinaryTree.__str__(self.getLeftChild())
            result += " " + str(self.getData())
            if(self.getRightChild() != None):
                result += " " + BinaryTree.__str__(self.getRightChild())
        return result

    def preorderTraversal(self):
        if (self.isEmpty()):
            return "Empty"

        else:
            result = " "
            result += str(self.getData())
            if (self.getLeftChild() != None):
                result += BinaryTree.__str__(self.getLeftChild())
            if (self.getRightChild() != None):
                result += " " + BinaryTree.__str__(self.getRightChild())
        return result

    def postorderTraversal(self):
        if (self.isEmpty()):
            return "Empty"

        else:
            result = " "
            if (self.getLeftChild() != None):
                result += BinaryTree.__str__(self.getLeftChild())
            if (self.getRightChild() != None):
                result += " " + BinaryTree.__str__(self.getRightChild())
            result += " " + str(self.getData())
        return result

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setLeftChild(self,data):
        self.leftChild = data

    def setRightChild(self,data):
        self.rightChild = data

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def tree_max(self):
        if not self:
            return float("-inf")
        maxleft = BinaryTree.tree_max(self.leftChild)
        maxright = BinaryTree.tree_max(self.rightChild)
        return max(self.data,maxleft,maxright)

    def tree_min(self):
        if not self:
            return float("inf")
        minleft = BinaryTree.tree_min(self.leftChild)
        minright = BinaryTree.tree_min(self.rightChild)
        return min(self.data,minleft,minright)

    def isBST(self):
        if not self:
            return True
        if (BinaryTree.tree_max(self.leftChild) <= self.data <= BinaryTree.tree_min(self.rightChild) and BinaryTree.isBST(self.leftChild) and BinaryTree.isBST(self.rightChild)):
            return True
        else:
            return False




#def main():
#    BT = BinaryTree()
#    print("isEmpty() = " + str(BT.isEmpty()))
#    print(BT)

#    BT.setData(101)
#    print("isEmpty() = " + str(BT.isEmpty()))
#    print(BT)

#    BT.setLeftChild(BinaryTree(50))
#    print(BT)

#    BT.setRightChild(BinaryTree(250))
#    print(BT)

#    BT.getLeftChild().setLeftChild(BinaryTree(42))
#    print(BT)

#    BT.getLeftChild().getLeftChild().setLeftChild(BinaryTree(31))
#    print(BT)

#    BT.getRightChild().setRightChild(BinaryTree(315))
#    print(BT)

#    BT.getRightChild().setLeftChild(BinaryTree(200))
#    print(BT)

#    print("Inorder traversal: " + str(BT))
#    print("Preorder traversal: " + BT.preorderTraversal())
#    print("Postorder traversal: " + BT.postorderTraversal())
#    print(BinaryTree.isBST(BT))
#main()