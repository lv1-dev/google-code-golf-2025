def p(g):
 u=10;a=sum(g,[])+[1]*u;o=range(u*u);n,*l=i=[r for r in o if a[r]&2];r=[e for e in o if all(u>e%u+r%u-n%u>=a[e-n+r]<1for r in i)][~n^51:]
 for e in r[:1]+r[-3:]:
  for r in i:r+=e-n;g[r//u][r%u]=2
 return g