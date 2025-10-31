def p(g):
 h=len(g);F=sum(g,[]);z=b=h*h
 while(F[b:=b-1]>0<F[b-2]==F[c:=b+~h*2]==F[c+2])<1:0
 while z:
  if v:=F[z:=z-1]:x=b+c-z;G=g[x//h];g[z//h][x%h]=G[z%h]=G[x%h]=v
 return g