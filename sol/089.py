def p(n):
 d={(i,f):e for i,p in enumerate(n)for f,e in enumerate(p)if e};t={};p=[]
 while d:
  for(i,f),e in(u:=[d.popitem()]):
   if 1<e<4:r,m,l=i,f,2*e-5
   u+=[((i+p,f+m),e)for m in(-1,0,1)for p in(-1,0,1)if(e:=d.pop((i+p,f+m),0))]
  if u[1:]:t[l]=[((i-r,f-m),e)for(i,f),e in u]
  else:p+=[(r,m,l)]
 for r,m,l in p:
  for(i,f),e in t[l]:n[r+i][m+f*l]=e
 return n