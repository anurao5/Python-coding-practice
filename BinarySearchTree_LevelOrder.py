#Every node contains data and reference to right and left nodes
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    #Insert a node into the tree
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


    def levelOrder(self, root):
        #Appends tree elements to a queue one level at a time
        if root is None:
            return

        bstQueue = []
        bstQueue.append(root)

        while(len(bstQueue) > 0):
            print(bstQueue[0].data, end=' ')
            node = bstQueue.pop(0)

            if node.left is not None:
                bstQueue.append(node.left)

            if node.right is not None:
                bstQueue.append(node.right)



T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)