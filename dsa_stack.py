#stack

class stack:

    p=-1
    s=[]

    def push(self,a):
        self.p=self.p+1
        self.s.append(a)
        
    def pop(self):
        
        print(self.s[self.p])
        self.p=self.p-1
        
    def isempty(self):
        
        if(self.p==-1):
            print("stack is empty")
        else:
            print("not empty")
    def top(self):
        print("stack top is: ",self.p)

if __name__=='__main__':

    st1 = stack()

    st1.push(1)
    st1.push(4)
    st1.pop()
    st1.pop()
    st1.top()
    st1.isempty()
    print(st1.s)
        
        


    
