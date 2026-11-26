from itertools import count
from reprlib import recursive_repr


class Node:

    def __init__(self,data):
        self.data =data
        self.left = self.right = None



class BST:

    def __init__(self):
        self.root = None


    def is_empty(self):
        return self.root is None


    def insert(self,new_node):

        if self.is_empty():
            self.root = new_node #BST IS EMPTY!
            return

        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp= temp.right


    def in_order(self,rt):
        if rt is None:
            return
        else:
            self.in_order(rt.left)
            print(rt.data,end=" ")
            self.in_order(rt.right)

    def pre_order(self,rt):
        if rt is None:
            return

        print(rt.data,end=" ")
        self.pre_order(rt.left)
        self.pre_order(rt.right)

    def post_order(self,rt):
        if rt is None:
            return

        self.post_order(rt.left)
        self.post_order(rt.right)
        print(rt.data,end=" ")

    def recurInsert(self,rt,newNode):
        if rt is None:
            self.root = newNode
            return


        if newNode.data < rt.data:
            if newNode.left is None:
                self.recurInsert(rt.left,newNode)
                rt.left = newNode
                return
        else:
            self.recurInsert(rt.right,newNode)
            rt.right = newNode


    def findMin_Max(self):
        temp = self.root
        while temp.left:
            temp=temp.left
        print("Min:",temp.data)
        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:",temp.data)

    #Learn deletion of a node

    def search(self,key):
        t = self.root

        while t:
            if key == t.data:
                return True
            elif key < t.data:
                t=t.left
            else:
                t=t.right

        return False

    def count(self,rt):
        if rt is None:
            return 0

        return 1 + self.count(rt.left) + self.count(rt.right)

    def countLeafNodes(self,rt):
        if rt is None:
            return 0
        if rt.left is None and rt.right is None:
    
         return self.countLeafNodes(rt.left) + self.countLeafNodes(rt.right)

    def countNonLeafNodes(self,rt):
        if rt is None:
            return 0

        if rt.left is not None or rt.right is not None:
            return 1

        return self.countNonLeafNodes(rt.left) + self.countNonLeafNodes(rt.right)

    #Level wise traversal
    def level_order(self,rt):
        if rt is None:
            print("BST is empty!")
            return

        arr = []
        count = 0

        arr.append(rt)

        while count < len(arr):
            temp = arr[count]
            print(f"Level {count} : {temp.data}",end=" ")
            count+=1
            if temp.left:
                arr.append(temp.left)
            if temp.right:
                arr.append(temp.right)

        print("\n-----------------------------")

bst = BST()
bst.insert(Node(100))
bst.insert(Node(10))
bst.insert(Node(450))
bst.insert(Node(0))
bst.insert(Node(65))
bst.insert(Node(300))
bst.in_order(bst.root)
print()
bst.level_order(bst.root)
print()
bst.pre_order(bst.root)
print()
bst.post_order(bst.root)
print()
print("------------------------------------")
print(bst.search(450))
print("Count of nodes",bst.count(bst.root))
bst.insert(Node(790))
bst.in_order(bst.root)
print()
print("Count of nodes",bst.count(bst.root))
print("Count of leaf nodes",bst.countLeafNodes(bst.root))
print("Count of non leaf nodes: ",bst.countNonLeafNodes(bst.root))

print("Nodes in left sub tree: ",bst.count(bst.root.left))