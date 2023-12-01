class Node:
    def __init__(self, label, docs=[]):
        self.label = label
        self.docs = docs
        self.left = self.right = None
    #--------------------------------------------
    def merge(self, node):
        self.docs += node.docs
        return self
    #--------------------------------------------
    def __str__(self):
        return f"{self.label} {self.docs}"
    #--------------------------------------------
#################################################
class Tree:
    def __init__(self):
        self.root = None
    #--------------------------------------------
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            self.__insert(self.root, node)
    def __insert(self, root, node):
        if root is None:
            root = node
        elif node.label == root.label:
            root = root.merge(node)         #merge nodes
        elif node.label < root.label:
            root.left = self.__insert(root.left, node)
        else:
            root.right = self.__insert(root.right, node)
        return root
    #--------------------------------------------
    def search(self, label):
        return self.__search(self.root, label)
    def __search(self, root, label):
        if root is None:
            return None
        if label == root.label:
            return root
        if label <= root.label:
            return self.__search(root.left, label)
        else:
            return self.__search(root.right, label)
    #--------------------------------------------
    def count(self):
        return self.__count(self.root)
    def __count(self, root):
        if root is None:
            return 0
        return 1 + self.__count(root.left) + self.__count(root.right)
    #--------------------------------------------
    def display(self):
        self.__display(self.root)
    def __display(self, root):
        if root == None: return
        self.__display(root.left)
        print(root)
        self.__display(root.right)
    #--------------------------------------------
#################################################