#fibonaci using dynamic programming

def fib(n,ar):
    
    if ar[n-1] is not None:
        return(ar[n-1])

    if(n==1 or n==2):

        return 1
    else:

        sum = fib(n-1,ar) + fib(n-2,ar)
        
    ar.append(sum)
    return(sum)

if __name__=='__main__':

    ar=[None for _ in range (15)]
    print(fib(15,ar))

