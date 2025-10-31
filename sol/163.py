def p(g):
 s=sum(g,[]);k=s.index(4);d,e=k//11&3,k%11&3;q=81
 while q:q-=1;a=q//9;b=q%9//3;g[a//3*4+b][a%3*4+q%3]=(a==d*3+e)*s[k+(b-d)*11+q%3-e]
 return g