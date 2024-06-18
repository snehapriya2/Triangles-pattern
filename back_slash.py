if int(i/2)%2 == 0:
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
