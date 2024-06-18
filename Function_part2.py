elif mode == 'd2':
        for i in range(c, c*r):
            if i in graph[i-c+1]:
                for j in graph[i-c+1]:
                    if j != i:
                        graph[i].append(j)
                        graph[j].append(i)
    return graph
