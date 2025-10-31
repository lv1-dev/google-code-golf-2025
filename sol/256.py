def p(g):
 d=sum(r:=max(g))//2;m=d+g.index(r)
 for r in g:r[:m]=[(m-d|8)//9+2]*m;m-=m>0
 return g