def p(g,r=range):
 o=len(g);m=len(g[0]);a=sum(g,[]);l=max(r(1,10),key=a.count)
 while l in a:
  i,t=divmod(a.index(l),m);f=[]
  def p(n,e):
   if o>n>=0<=e<m and(u:=a[n*m+e]):
    f[:]=f+[(n-i,e-t,u)];g[n][e]=a[n*m+e]=0
    for d in-1,1:p(n+d,e);p(n,e+d)
  p(i,t)
  for n in r(o):
   for d in-1,1:
    for e in r(m):
     if all(o>n+i>=0<=e+t*d<m and u in(l,g[n+i][e+t*d])for i,t,u in f):
      for i,t,u in f:g[n+i][e+t*d]=u
  f=[(-t,i,u)for i,t,u in f]
  for n in r(o):
   for d in-1,1:
    for e in r(m):
     if all(o>n+i>=0<=e+t*d<m and u in(l,g[n+i][e+t*d])for i,t,u in f):
      for i,t,u in f:g[n+i][e+t*d]=u
  f=[(-t,i,u)for i,t,u in f]
  for n in r(o):
   for d in-1,1:
    for e in r(m):
     if all(o>n+i>=0<=e+t*d<m and u in(l,g[n+i][e+t*d])for i,t,u in f):
      for i,t,u in f:g[n+i][e+t*d]=u
  f=[(-t,i,u)for i,t,u in f]
  for n in r(o):
   for d in-1,1:
    for e in r(m):
     if all(o>n+i>=0<=e+t*d<m and u in(l,g[n+i][e+t*d])for i,t,u in f):
      for i,t,u in f:g[n+i][e+t*d]=u
  f=[(-t,i,u)for i,t,u in f]
 return g