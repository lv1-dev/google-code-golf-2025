def p(f):
 g=min(e:=sum(f,[]),key=e.count);i=sum(g in r for r in zip(*f))-2;h=sum(g in r for r in f)-2
 for n in range(21-i):
  for p in range(21-h):
   if all(sum(r[n:n+i])==0for r in f[p:p+h]):
    for r in f[p-1],f[p+h]:r[n:n+i]=[g]*i
    for r in f[p-1:p+h+1]:r[n-1]=r[n+i]=g
 return f