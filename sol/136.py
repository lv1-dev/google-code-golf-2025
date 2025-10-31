def p(g):
 for s in-1,1:
  i,j=divmod(sum(g,[]).index(s%3),10)
  while~i*~j%11:g[i][j]=s%3;i-=s;j-=s
 return g