# author : NIHAR MUKHIYA
# date : 18/09/2018
# description : implementation of various operations of BST such as
#               insertion, deletion, max-min value, parent-of-a-node, inorder, preorder, postorder
#               in python


import sys


class avl(object):
    def __init__(self, val):
        self.rc = None
        self.lc = None
        self.val = val
        self.height = 1
        self.balance = 0

    def insert(self, val):
        if (self.val):
            if (val < self.val):
                if (self.lc is None):
                    self.lc = avl(val)
                else:
                    self.lc.insert(val)
            elif (val > self.val):
                if (self.rc is None):
                    self.rc = avl(val)
                else:
                    self.rc.insert(val)
            else:
                self.val = val
        self.rebalance()

    def rebalance(self):
        self.update_heights()
        self.update_balances()
        print(self.balance)
6        if(self.balance < -1 or self.balance > 1):
            if self.balance > 1:
                if self.lc.balance < 0:
                    self.lc.rotateLeft()
                    self.update_heights()
                    self.update_balances()
                self.rotateRight()
                self.update_heights()
                self.update_balances()
            if self.balance < -1:
                if self.rc.balance > 0:
                    self.rc.rotateRight()
                    self.update_heights()
                    self.update_balances()
                self.rotateLeft()
                self.update_heights()
                self.update_balances()


    def rotateLeft(self):
            """
            Left rotation
                set self as the left subtree of right subree
            """
            if self:
                new_root = self.rc
                new_left_sub = new_root.lc.val
                old_root = self

                self.val = new_root
                old_root.rc.val = new_left_sub
                new_root.lc.val = old_root
            else:
                return

    def rotateRight(self):
        """
        Right rotation
            set self as the right subtree of left subree
        """
        if self:
            new_root = self.lc
            if new_root.rc:
                new_left_sub = new_root.rc.val
                old_root = self

                self.val = new_root
                old_root.lc.val = new_left_sub
                new_root.rc.val = old_root
        else:
            return 0

    def getHeight(self, temp):
        if not temp:
            return 0
        else:
            return temp.height

    def update_heights(self):
        if self.val:
            print(self.val)
            if (self.lc != None or self.rc != None):
                if self.lc:
                    self.lc.update_heights()
                if self.rc:
                    self.rc.update_heights()
                self.height = 1 + max(self.getHeight(self.lc), self.getHeight(self.rc))
            else:
                self.height = 1
        else:
            self.height = 1

    def update_balances(self):
        if self.val:
            if self.lc:
                self.lc.update_balances()
            if self.rc:
                self.rc.update_balances()
            self.balance = self.getHeight(self.lc) - self.getHeight(self.rc)
        else:
            self.balance = 0

    def minValue(self, node):
        current = node
        while (current.lc is not None):
            current = current.lc
        return current


    def findParent(self, val):
        parent = None
        while True:
            if (self.val is None):
                return (None, None)
            if (self.val == val):
                return (parent, self)
            if (self.val < val):
                parent, self = self, self.rc
            else:
                parent, self = self, self.lc


    def inorder(self):
        if (self.val):
            if (self.lc):
                self.lc.inorder()
            print(self.balance)
            if (self.rc):
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

while (1):
    z = input(
        "Enter your choice\n 1. Insert\n2.smallest element\n 3. Inorder\n 4. Preorder\n 5. Postorder\n 6.Delete\n7. Exit\n8.balance factor of a node\n")
    if (z == '1'):
        b = int(input("enter the number of elements to be inserted"))
        while (b > 0):
            c = int(input("enter elements: "))
            root.insert(c)
            b -= 1

    elif (z == '2'):
        y = root.minValue(root)
        print("The smallest element in BST is: " + str(y) + "/n")

    elif (z == '3'):
        print("INORDER is: ")
        root.inorder()

    elif (z == '4'):
        print("PREORDER is: ")
        root.preorder()

    elif (z == '5'):
        print("POSTORDER is: ")
        root.postorder()

    elif (z == '6'):
        g = int(input("enter element to be deleted: "))

        v = root.deleteNode(g)


    elif (z == '7'):
        sys.exit()
    elif (z == '8'):
        if (root.val):
            if (root.lc):
                root.lc.inorder()
            print(root.val, root.balance)
            if (root.rc):
                root.rc.inorder()
        else:
            print("Tree is Empty")



    else:
        print("wrong input!!")
