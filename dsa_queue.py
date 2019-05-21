#queue

class queue:

    p=-1
    s=[]

    def enque(self,a):

        self.s.append(a)

    def deque(self):

        self.p=self.p+1
        print(self.s[self.p])
        
    def isempty(self):
        if(self.p == (len(self.s)-1)):
            print("queue is empty")
        else:
            print("queue is not empty")
    def einque(self):

        print("elements left in a queue are: ",end="")
        print(self.s[self.p+1:])

if __name__=='__main__':

    q=queue()

    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.deque()
    q.isempty()
    q.einque()


        
