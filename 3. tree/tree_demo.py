from Tree import Tree, Node
tree = Tree()

tree.insert(Node("hello"))
tree.insert(Node("welcome", [0, 1]))
tree.insert(Node("bye", [1]))
tree.insert(Node("bye", [2]))

tree.display()
print("Nodes", tree.count())

print(tree.search("AHMED"))
print(tree.search("hello"))