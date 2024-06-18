else:
        j = 0
        R1 = int((i-1)/2)*c
        R2 = int((i+1)/2)*c
        if int(i/2)%2 == 1:
            
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
    
