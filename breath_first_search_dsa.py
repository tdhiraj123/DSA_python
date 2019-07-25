# BFS test-1

d={1:[2,3],2:[1,4],3:[1,5,6],4:[],5:[3,7],6:[],7:[]}
vis=[1]
p=0
ind=1

def bfs(d,ind,p):

    if len(vis)==p+1 and p != 0:
        print(vis)
        return True

    lis=d[ind]
    for i in lis:
        if i not in vis:
            vis.append(i)
    p=p+1
    bfs(d,vis[p],p)
    return True

bfs(d,ind,p)

        

