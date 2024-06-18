def expand(c, r, graph, mode):
    if mode == 'h':
        for i in range(r):
            for j in range(2, c):
                if i*c+j in graph[i*c+j-2]:
                    for k in graph[i*c+j-2]:
                        if k != i*c+j:
                            graph[i*c+j].append(k)
                            graph[k].append(i*c+j) 
    elif mode == 'd1':
        for i in range(c+1, c*r):
            if i in graph[i-c-1]:
                for j in graph[i-c-1]:
                    if j != i:
                        graph[i].append(j)
                        graph[j].append(i)
    elif mode == 'd2':
        for i in range(c, c*r):
            if i in graph[i-c+1]:
                for j in graph[i-c+1]:
                    if j != i:
                        graph[i].append(j)
                        graph[j].append(i)
    return graph
#spliting is done by space
r, c = [int(x) for x in input().split(' ')]
shape = []
#input the 2*r-1 values by pressing enter each time
for i in range(2*r-1):
    shape.append(input())
h = [[] for j in range(c*r)]            #creating list for each element
d1 = [[] for j in range(c*r)] #\\\\
d2 = [[] for j in range(c*r)] #////
for i in range(2*r-1):
    if i%2==0:
        R = int(i/2)*c
        p = shape[i].split('x')[1:-1]
        #print(p)
        if not shape[i][0] == 'x':
            j = 0
            for line in p:
                if line == '---':
                    print([R+2*j+1, R+2*j+3])
                    h[R+2*j+1].append(R+2*j+3)
                    h[R+2*j+3].append(R+2*j+1)
                j+=1       
        else:
            j = 0
            for line in p:
                if line == '---':
                    #print([R+2*j, R+2*j+2])
                    h[R+2*j].append(R+2*j+2)
                    h[R+2*j+2].append(R+2*j)
                j+=1
    else:
        j = 0
        R1 = int((i-1)/2)*c
        R2 = int((i+1)/2)*c
        if int(i/2)%2 == 1:
            #print('='*5,i,'='*5)
            for line in shape[i]:
                if line == '/':
                    J = int(j/4)*2
                    #print([R1+J+1,R2+J])
                    d2[R1+J+1].append(R2+J)
                    d2[R2+J].append(R1+J+1)
                elif line=='\\':
                    J = (int(j/4) + 1)*2 - 1
                    #print([R1+J,R2+J+1])
                    d1[R1+J].append(R2+J+1)
                    d1[R2+J+1].append(R1+J)
                j+=1
        if int(i/2)%2 == 0:
            #print('='*5,i,'='*5)
            for line in shape[i]:
                if line == '\\':
                    J = (int(j/4))*2
                    #print([R1+J,R2+J+1])
                    d1[R1+J].append(R2+J+1)
                    d1[R2+J+1].append(R1+J)
                elif line=='/':
                    J = (int(j/4) + 1)*2
                    #print([R1+J,R2+J-1])
                    d2[R1+J].append(R2+J-1)
                    d2[R2+J-1].append(R1+J)
                j+=1
h = expand(c,r,h,'h')
d1 = expand(c,r,d1,'d1')
d2 = expand(c,r,d2,'d2')
ans = 0
for i in range(r):
    for j in range(c):
        for k in h[i*c+j]:
            if k > i*c + j:
                K = k%c
                p1 = (i + int((K-j)/2))*c + int((K+j)/2)
                if p1 in d1[i*c+j]:
                    if p1 in d2[k]:
                        ans += 1
                p1 = (i - int((K-j)/2))*c + int((K+j)/2)
                if p1 in d2[i*c+j]:
                    if p1 in d1[k]:
                        ans += 1
print(ans)
