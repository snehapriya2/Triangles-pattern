r,c = [int(x) for x in input().split(' ')]
shape = []
for i in range(2*r-1):
    shape.append(input())
h = [[] for j in range(c*r)]
d1 = [[] for j in range(c*r)]
d2 = [[] for j in range(c*r)]
for i in range(2*r-1):
    if i%2 == 0:
        R = int(i/2)*c
        p = shape[i].split('x')[1:-1]
        #print(p)
        if not shape[i][0] == 'x':
            j = 0
            for line in p:
                if line =='---':
                    #print([R+2*j+1, R+2*j+3])
                    h[R+2*j+1].append(R+2*j+3)]
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
