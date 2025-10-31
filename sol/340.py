def p(a):
 for q in a[1:-1]:
  for v in q[(j:=1):-2]:q[j]=0;u,w=v!=a[0][1],v!=q[0];a[1-3*u][j]+=v*(v==a[-u][1]);q[1-3*w]+=v*(v==q[-w]);j+=1
 return a