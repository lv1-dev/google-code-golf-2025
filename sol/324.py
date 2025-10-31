def p(a):
 f=sum(a,[]);t=u,r=sorted({*f},key=f.count)[-2:];c=*zip(*a),;d=set()
 for i,n in enumerate(a):
  for o,e in enumerate(n):
   if u!=e!=r:d|={i+o,i-o<<6};t[n.count(r)*c[o].count(r)>2*n.count(u)*c[o].count(u)]=e
 for i,n in enumerate(a):
  for o,e in enumerate(n):
   if{i+o,i-o<<6}&d:n[o]=t[n.count(r)*c[o].count(r)>2*n.count(u)*c[o].count(u)]
 return a