#-------------------------- BINARY TREE ------------------------#
"""

Full Binary Tree
- Each node has either 0 or 2 children.
- No node has a single chil.

Complete Binary tree
- All levelexcept possibly the last are completely filled.
- Nodes inthe last level are filled from left to right.

Perfect Binary 
- All internal nodes have exactil 2 nodes.
- All leaf nodes are at the same level.

= Creation of tree
= Insertion of a node
= Deletion of a node
= Search for a value
= Traverse all nodes 
= Deletion of tree

Traversal  :-

1. Preorder (Root - Left - Right)
2. Inorder  (Left - Root - Right)
3. Postorder (Left - Right - Root)

Binary Search Tree :-
- It perform faster BT when inserting and deleting nodes.


"""

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
            print(" The value not found")
        else:
            insertNode(rootNode.rightChild, nodeValue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)


newBST = BSTNode(None)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
insertNode(newBST, 10)

preOrderTraversal(newBST)
print()
inOrderTraversal(newBST)
print()
postOrderTraversal(newBST)
print()


searchNode(newBST, 100)