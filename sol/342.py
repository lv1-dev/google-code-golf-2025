def p(g):
 s=sum(g,[]);i=s.index;j=i(8);d=10
 for v in{*s}-{8}:k=i(v);g[k//d][k%d],g[j//d+(k>j)][j%d+(k%d>j%d)]=0,v
 return g