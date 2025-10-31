def p(j):
 f=min(e-1 for e,i in enumerate(j)for r,i in enumerate(i)if i==8)
 x=min(r-1 for e,i in enumerate(j)for r,i in enumerate(i)if i==8)
 n=max(e for e,i in enumerate(j)for r,i in enumerate(i)if i==8)-f+1
 p=min(e for e,i in enumerate(j)for r,i in enumerate(i)if i%8)
 a=min(r for e,i in enumerate(j)for r,i in enumerate(i)if i%8)
 return[[j[p+e][a+r]or(0<r<n<j[f+e][x+r])and[j[p+(t:=(i:=e+r>n)*n,i:=(e>r)^i)[i]][a+t**i],8][r in(e,n-e)]for r in range(n+1)]for e in range(n+1)]