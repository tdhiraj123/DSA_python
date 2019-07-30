# min coin change dynamic
#bottum-up

coin =list(map(int,input('coins:').split()))
amt=int(input('amt:'))

arr=[(amt+1) for _ in range(amt+1)]
arr[0]=0
for i in range(1,amt+1):
    
    mi=[]
    for j in coin:
        
        co=amt+1
        a=i
        if(j<=i):
            co=1+arr[a-j]
        mi.append(co)
    
    arr[i]=min(min(mi),arr[i])
print(arr[len(arr)-1])
            
        
            
            
            

            

        
        
