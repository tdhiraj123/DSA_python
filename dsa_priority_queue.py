# priority queue

class pri_que:

    def __init__(self):

        self.a=[]

    def enque(self,e):

        self.a.append(e)
        
    def delete(self):


        m=max(self.a)
        n=0
        m1=0
        for i in range(0,len(self.a)):

            if(self.a[i]==m):
                m1=i

                del self.a[m1]
                break
if __name__ =='__main__':

    pq=pri_que()

    pq.enque(1)
    pq.enque(2)
    pq.delete()
    pq.enque(3)
    pq.enque(7)
    pq.enque(2)
    pq.delete()
    print(pq.a)
    

    
