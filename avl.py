# author : NIHAR MUKHIYA
# date : 18/09/2018
# description : implementation of various operations of BST such as
#               insertion, deletion, max-min value, parent-of-a-node, inorder, preorder, postorder
#               in python


import  sys
"""
    def deleteNode(self, val):
        parent, node = self.findParent(val)

        # if node has no children
        if(node.lc is None and node.rc is None):
            if(parent):
                if(parent.lc is node):
                    parent.lc = None
                else:
                    parent.rc = None

            # if node with no children is root itself
            else:
                self.val = None
            del node
        # if node has one child
        elif(self.lc is not None or self.rc is not None):
            if(node.lc):
                t = node.lc
            else:
                t = node.rc

            if(parent):
                if(parent.lc is node):
                    parent.lc = t
                else:
                    parent.rc = t
            # if node with one child that is deleted is root itself
            else:
                self.lc = t.lc
                self.rc = t.rc
                self.val = t.val

            del node
        # if node has two children
        else:
            
            temp = self.minValue(self.rc)
            self.val = temp.val
            self.rc = self.rc.delete(temp.val)
            
            node = parent
            successor = node.rc
            while(successor.lc):
                parent = successor
                successor = successor.lc
            print(successor.val)
            node.val = successor.val
            if(parent.lc == successor):
                parent.lc = successor.rc
            else:
                parent.rc = successor.rc
"""

class avl(object):
    def __init__(self, val):
        self.rc = None
        self.lc = None
        self.val = val
        self.height = -1
        self.balance = 0

    def insert(self, val):
        if(self.val):
            if(val<self.val):
                if(self.lc is None):
                    self.lc = avl(val)
                else:
                    self.lc.insert(val)
            elif(val>self.val):
                if(self.rc is None):
                    self.rc = avl(val)
                else:
                    self.rc.insert(val)
            else:
                self.val = val

    def rebalance(self):
        self.update_heights(recursive=False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.lc.rotate_left()
                    self.update_heights()
                    self.update_balances()

            self.rotate_right()
            self.update_heights()
            self.update_balances()

            if self.balance < -1:
                if self.rc.balance > 0:
                    self.rc.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):

        if self:
            if recursive:
                if self.lc:
                    self.lc.update_heights()
                if self.rc:
                    self.rc.update_heights()

            self.height = 1 + max(self.lc.height, self.rc.height)
        else:
            self.height = -1

    def update_balances(self, recursive=True):

        if self:
            if recursive:
                if self.lc:
                    self.lc.update_balances()
                if self.rc:
                    self.rc.update_balances()

            self.balance = self.lc.height - self.rc.height
        else:
            self.balance = 0

    def rotate_right(self):

        new_root = self.lc
        new_left_sub = new_root.rc
        old_root = self

        self = new_root
        old_root.lc = new_left_sub
        new_root.rc = old_root


    def rotate_left(self):

        new_root = self.rc
        new_left_sub = new_root.lc
        old_root = self

        self = new_root
        old_root.rc = new_left_sub
        new_root.lc = old_root

    def minValue(self, node):
        current = node
        while(current.lc is not None):
            current = current.lc
        return current

    def findParent(self, val):
        parent = None
        while True:
            if(self.val is None):
                return (None, None)
            if(self.val == val):
                return (parent, self)
            if(self.val < val):
                parent, self = self, self.rc
            else:
                parent, self = self, self.lc

    def inorder(self):
        if(self.val):
            if(self.lc):
                self.lc.inorder()
            print(self.val)
            if(self.rc):
                self.rc.inorder()
        else:
            print("Tree is Empty")

    def preorder(self):
        print(self.val)
        if (self.lc):
            self.lc.preorder()
        if (self.rc):
            self.rc.preorder()

    def postorder(self):
        if (self.lc):
            self.lc.postorder()
        if (self.rc):
            self.rc.postorder()
        print(self.val)


a = int(input("enter root"))
root = avl(a)



while(1):
    z = input("Enter your choice\n 1. Insert\n2.smallest element\n 3. Inorder\n 4. Preorder\n 5. Postorder\n 6.Delete\n7. Exit\n8.balance factor of a node\n")
    if (z == '1'):
        b = int(input("enter the number of elements to be inserted"))
        while (b > 0):
            c = int(input("enter elements: "))
            root.insert(c)
            b -= 1

    elif(z == '2'):
        y = root.minValue(root)
        print("The smallest element in BST is: " +str(y)+ "/n")

    elif (z == '3'):
        print("INORDER is: ")
        root.inorder()

    elif(z== '4'):
        print("PREORDER is: ")
        root.preorder()

    elif(z=='5'):
        print("POSTORDER is: ")
        root.postorder()

    elif(z == '6'):
        g = int(input("enter element to be deleted: "))

        v = root.deleteNode(g)


    elif(z=='7'):
        sys.exit()
    elif(z == '8'):
        if(root.val):
            if(root.lc):
                root.lc.inorder()
            print(root.val, root.balance)
            if(root.rc):
                root.rc.inorder()
        else:
            print("Tree is Empty")



    else:
        print("wrong input!!")
