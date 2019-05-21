# dynamic array

class dynamic:

    
    def __init__(self):
        
        self.n=0
        self.a=[0]
        self.c=1
        

    def append(self,e):

        if(self.n==len(self.a)):
            for i in range(0,len(self.a)):
                self.a.append(0)
                self.c=self.c+1
        self.a[self.n]=e
        self.n=self.n+1

        print("the element {} is added to the list".format(e))

    def eleat(self,i):

        print("element at {} is {}".format(i,self.a[i]))

    def cap(self):
        print("the capacity is ",self.c)

if __name__=='__main__':

    da=dynamic()

    da.append(1)
    da.cap()
    da.append(2)
    da.cap()
    da.append(3)
    da.cap()
    da.append(4)
    da.append(5)
    da.append(6)
    da.append(7)
    da.cap()
    print(da.a)

    da1=dynamic()
    print(da1.c)
    print(da1.a)
    
    
            

            
