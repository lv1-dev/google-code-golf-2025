def p(p):
 u=len(p[0]);r=range(len(p:=sum(p,[])));g,f,e,i=i=[i for i in r if p[i]]
 for i in i:
  for n in 1,u-1,u,-u-1:p[i+n]=p[i-n]=p[g]^p[f]^p[i]
 for g,f,i in(g,f,1),(g,e,u),(e,i,1),(f,i,u):
  while(g:=g+2*i)<=(f:=f-2*i):p[g]=p[f]=5
 return[p[i:i+u]for i in r[::u]]