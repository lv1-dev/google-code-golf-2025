def p(g,E=enumerate,*S):
 for d in-1,8:
  for r,R in E(g):
   for c,v in E(R):
    for x,y,v in S*(d==v):g[r+x-a][c+y-b]=v
    if d&v&7:S+=(r,c,v),;R[c]=0;a,b,_=S[0]
 return g