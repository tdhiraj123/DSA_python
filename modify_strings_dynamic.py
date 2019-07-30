# modifing string_1 to string_2 using 3 operations (modify,insert and delete)
# edit distance


s1=input('enter s1:')
s2=input('enter s2:')
# a= [[0]*(len(s1)+1)]*(len(s2)+1)
a=[[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
for i in range(len(s1)+1):
    
    a[0][i]=i
    a[i][0]=i

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):

        if(s1[i-1]==s2[j-1]):

           a[i][j]=a[i-1][j-1]
        else:

           a[i][j]=min(a[i-1][j-1],a[i-1][j],a[i][j-1])+1
print(a[len(s1)][len(s2)])


    
