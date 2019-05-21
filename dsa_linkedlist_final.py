#linked list

class node:

    def __init__(self,dv=None):

        self.dv = dv
        self.nv= None


class Flinkedlist:

    def __init__(self):
        self.hv=None

    def printl(self):

        v=self.hv
        while v is not None:

            print(str(v.dv)+" ",end='')

            v=v.nv

    def insert(self,data,next_to=None):

        nn=node(data)
        #inserting when list is empty
        if self.hv is None:
            self.hv = nn
            return

        #inserting at index and 0 shoud be passed in next_to
        elif(next_to == 0):
            nn.nv=self.hv
            self.hv=nn

        #inserting at the end and only one parameter should be passed
        elif(next_to == None):

            lastn = self.hv
            while(lastn.nv):
                lastn = lastn.nv
            lastn.nv=nn

        #inserting next to some node 
        else:
            #x = self.hv
            nn.nv=next_to.nv
            next_to.nv = nn

    def remove(self,n): # in place of n the data value need to be sent not node name !!

        #removing first node
        if(self.hv.dv == n):
            
            self.hv=self.hv.nv

        #removing other nodes
        else:

            x=self.hv
            y=self.hv
            while(x.nv):
                x=x.nv
                if(x.dv == n):
                    y.nv=x.nv
                y=y.nv


                    

        
l=Flinkedlist()

l.hv=node(1)
n2=node(2)
n3=node(3)

l.hv.nv=n2
n2.nv=n3
l.insert(6,n2)
l.insert(7)
l.insert(9,0)
l.remove(2)
l.remove(9)
l.remove(7)

l.printl()
