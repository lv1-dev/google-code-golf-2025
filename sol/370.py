def p(i):
 h,e,n=max(r:=[(i[p][g],p,g)for p in range(len(i))for g in range(len(i[0]))if i[p][g]^i[0][0]]);f,e,n=max((((e-p)*(n-g))**2,e-p,n-g)for p,p,g in r)
 for p,p,g in r:
  while(p:=p+e)in range(len(i))and(g:=g+n)in range(len(i[0])):i[p][g]=h
 return i