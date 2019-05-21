# dsa searching algorithms

# 1. linear search

arr = list(map(int,input("enter numbers: ").split()))
ele = int(input("number need to be find: "))


def linear(arr,e):

    for i in range(0,len(arr)):

        if e==arr[i]:

            return i
    return -1

#print("the element is found at ",linear(arr,ele))



# 2. bubble sort using while loop

def Bubble(arr,e):


    fir=0
    end=len(arr)-1
    

    while fir<=end :
        mid=(fir+end)//2
        if arr[mid]==e:

            return mid

        elif e<arr[mid]:
            end=mid-1
        elif e>arr[mid] :
            fir=mid+1
    return -1

print("the value is found at bubble",Bubble(arr,ele))





# 2 b. bubble sort using recursion
# not complete.

def r_bubble(arr,e):

    fir=0
    end = len(arr)-1

    mid = (fir+end)//2
    print(arr)
    
    
    if arr[mid]== e:

        print("recurssion ans ",mid)
        exit()
        

    elif e>arr[mid]:

        fir=mid+1
        if len(arr) ==2 :
            if arr[fir]==e:
                return(fir)
            else:
                return(-1)
               
        
        r_bubble(arr[fir:end+1],e)
        

    elif e<arr[mid]:

        end=mid-1
        if len[arr] ==2 and arr[end]==e:
            return(fir)
        r_bubble(arr[fir:end+1],e)
        
   
    return -1

r_bubble(arr,ele)

    
    





    
    
