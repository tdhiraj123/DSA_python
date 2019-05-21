#binary tree

class Node:

    def __init__(self,data):

        self.left = None
        self.right = None

        self.data = data

    def insert(self,data):

        if self.data:

            if data<self.data:

                if self.left is None:

                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:

                if self.right is None:

                    self.right=Node(data)

                else:
                    self.right.insert(data)
        else:
            self.data=data

            
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(str(lkpval)+" Not Found")
                return
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(str(lkpval)+" Not Found")
                return
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

            
    def PT(self):

        if self.left:
            self.left.PT()
        print(self.data)

        if self.right:
            self.right.PT()

root = Node(6)
root.insert(1)
root.insert(4)
root.insert(8)
root.insert(9)

root.PT()
root.findval(4)
root.findval(5)
root.findval(1)
