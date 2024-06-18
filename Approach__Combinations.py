import math 
r = int(input("enter no:of rows:"))
c = int(input("enter no:of columns:"))
lst = []
total = 0
for z in range(0,r):
    print("enter no:of 'x' characters in line {z}:")
    lst.append(int(input()))
    #we get the lst of no:of vertices of triangles.
    total += lst[z]
print(total)
# nCr = n!/((n-r)!r!)
total_tri = math.factorial(total)/(math.factorial(r)*math.factorial(total-r))
print("total no:of triangles that are possible:")
print(total_tri)



#no:of triangles that are not valid from lines are:
trashtri =[]
for z in range(0,r):
    print("enter no:of 'x' characters in line")
    trashtri.append(int(input()))
    delete = math.factorial(trashtri[z])/(math.factorial(r)*math.factorial(trashtri[z]-r))
    total_tri -=delete
print(total_tri)

#Number of Diagonals = n(n-3)/2


    
