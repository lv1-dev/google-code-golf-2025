def p(a,d=enumerate):
 (u,m,r),(l,d,o)=((p,f,u)for(p,u)in d(a)for(f,u)in d(u)if u)
 if u^l:return*zip(*p([*map(list,zip(*a))])),
 t=d-m>>1;a[u][m:d+1]=[r]*t+[0,0]+[o]*t
 for f in-2,-1,1,2:a[u+f][m+t-1:m+t+3]=r,~f%2*r,~f%2*o,o
 return a