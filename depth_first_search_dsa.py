# depth first search test-1
d={0:[1,2],1:[0,3],2:[0,4,5],3:[],4:[2,6],5:[],6:[]}
vis=[0]
t=[0]
p=0
ind=0
def dfs(d,vis,ind):

    

    if len(vis)==0 :
        return True

    p= vis.pop()
    print(p)

    lis=d[p]
    for i in lis:
        if i not in t:
            vis.append(i)
            t.append(i)
    
    dfs(d,vis,ind)
    return True

dfs(d,vis,ind)
