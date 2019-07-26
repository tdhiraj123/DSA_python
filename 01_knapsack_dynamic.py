# 0/1 knapsack romba fun

mweig =int(input('max weight:'))
weight=list(map(int,input().split()))
value=list(map(int,input().split()))

dp=[[0 for _ in range(mweig+1)] for _ in range(len(weight)+1)]

for i in range(1,len(dp)):

    w=weight[i-1]
    v=value[i-1]
    
    for j in range(1,len(dp[0])):

        x=max([dp[i-1][j],dp[i][j-1]])

        if(w==j):
              x=max([x,v])

        if(j>w):

              t=dp[i][j-w]+dp[i][w]
              x=max([x,t])
        dp[i][j]=x
print(dp[len(weight)][mweig])

              

                                                                                                                                                                                                                                          
        

        

        

        
