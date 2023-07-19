def pr(n):
    fl=1
    for i in range(2, n//2+1):
        if n%i==0:
            fl=0
    return fl
for i in range(145274, 273921):
    k=0
    k19=0
    for j in range(2, i//2+1):
        if i%j==0 and pr(j)==1:
            k+=1
        if i%j==0 and j%19==0:
            k19+=1
        if k==5 and k19==7:
            print(i)
            break