class Node:
    def __init__(self, label, docs=[]):
        self.label = label
        self.docs = docs
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.label} {self.docs}"
#------------------------------------
def insert(root, node):
    if root is None:
        root = node
    elif node.label <= root.label:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)
    return root
#------------------------------------
def display(root):
    if root == None: return
    display(root.left)
    print(root)
    display(root.right)
#------------------------------------
def search(root, value):
    if root is None:
        return None
    if root.label == value:
        return root
    if value <= root.label:
        return search(root.left, value)
    else:
        return search(root.right, value)
#------------------------------------
docs = [
    "Ahmed Mohamed",
    "Saeed Mohamed",
    "Ahmed Mohamed Saeed",
]
root = None
for i, doc in enumerate(docs):
    for word in doc.split(" "):
        if root is None:
            root = Node(word, [i])
        else:
            node = search(root, word)
            if node:
                node.docs += [i]
            else:
                insert(root, Node(word, [i]))
display(root)
# node = search(root, "Mohamed")
# node.docs += [99]
# display(root)

#------------------------------------
#------------------------------------