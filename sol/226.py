def p(g):
 for n in(s:=[1,615,342,338,278,274]):
  if(j:=n>>2&15)<10>(i:=n>>6)>=g[i][j]<1:g[i][j]=n&3;s+=n+4,n-4,n+64,n-64
 return g