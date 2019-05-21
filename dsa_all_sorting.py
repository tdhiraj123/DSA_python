# selection sort
# sotring algo 1

arr = list(map(int,input("array: ").split()))



def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    return arr

def selection_sort(arr):

    for i in range(0,len(arr)):

        m=min(arr[0+i:])

        for j in range(i,len(arr)):

            if(m==arr[j]):
                swap(arr,i,j)
                
                
    print(arr)

#print("selection")

#selection_sort(arr)





#bubble sort
#sorting algo 2


def Bubble_sort(arr):

    for i in range(0,len(arr)-1):
        for j in  range(0,len(arr)-1-i):

            if(arr[j]>arr[j+1]):
                swap(arr,j,j+1)
    
    print(arr)
#print("bubble")
#Bubble_sort(arr)





#insertion sort
# sorting algo 3

def sort(arr):

    for i in range(1, len(arr)): 
  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return(arr)
#print("insertion ",sort(arr))




# Merge sort
# sorting algo 4

 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:] 
        #print("L",L)
        mergeSort(L)
        #print("R",R)
        mergeSort(R)
        #print("hi")
        i = j = k = 0
        #print(arr)
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
                #print("left add",arr)
            else: 
                arr[k] = R[j] 
                j+=1
                #print("right add",arr)
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
            #print("left check",arr)
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
            #print("right check",arr)
    return arr
print(mergeSort(arr))



        




