def p(a):
 g=[]
 for r in a:
  for d in range(len(g)):
   for e in range(len(r)+1):
    for f in range(e):
     if all(g[d][f:e]+r[f:e])>any(r[e+1:e+2]+r[f-2:f:2]+[any(l[f:e])|(l+[5])[f-1]*(l+[5])[e]-25for l in g[d+1:]]):
      for l in g[d+1:]:l[f:e]=[4]*(e-f)
  g+=[r]
 return a