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
