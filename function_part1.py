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
    return graph
