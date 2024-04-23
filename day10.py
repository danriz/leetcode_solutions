import string

nmychar='A'
arr = [[nmychar for i in range(8)] for j in range(8)]
alphalist2=string.ascii_uppercase

assigment_counter= 0

m=0
n=len(arr)
total_cell=len(arr)*len(arr[0])
jj=0

while(total_cell>assigment_counter):
    for h1 in range(m,n):
        arr[m][h1] = alphalist2[assigment_counter%len(alphalist2)]
        assigment_counter=assigment_counter+1
    m=m+1

    for h1 in range(m,n):
        arr[h1][n-1] = alphalist2[assigment_counter%len(alphalist2)]
        assigment_counter=assigment_counter+1
    m=m-1
    n=n-1

    for h1 in range(n-1,m-1,-1):
        arr[n][h1] = alphalist2[assigment_counter%len(alphalist2)]
        assigment_counter=assigment_counter+1
    m=m+1


    for h1 in range(n-1,m-1,-1):
        arr[h1][m-1] = alphalist2[assigment_counter%len(alphalist2)]
        assigment_counter=assigment_counter+1

for x in range(len(arr)):
    for y in range(len(arr[0])):
        print(arr[x][y],end='')

    print()
