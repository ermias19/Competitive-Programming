class binrayTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=binrayTree(1)
root.left=binrayTree(2)
root.right=binrayTree(3)
root.left.left=binrayTree(4)
root.right.right=binrayTree(5)
root.left.rigth=binrayTree(6)


def bfs(root):
    if root:
        queue=[root]
        while queue:
            node=queue.pop(0)
            print(node.data,end=' ')
            if node.left:
                # print(node.data)
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # print(node.data)   

print(bfs(root))    