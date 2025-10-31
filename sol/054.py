def p(t):
 r=t[0][0];p=[o[:]for o in t];a,i=next((a,i)for a in range(28) for i in range(28) if(e:=(o:=p[a])[i])^r and(g:=(y:=(n:=p[a-1])[i])==p[a+1][i]==p[a-2][i]!=e)+(l:=(f:=o[i-1])==o[i+1]==o[i-2]!=e)and(n:=n[i-1])-(f,y)[g]);o[i]=r
 for w in t[a-2:a+3]:w[i-2:i+3]=r,r,r,r,r
 for(a,i)in((a,i)for a in range(28) for i in range(28) if(o:=p[a])[i]==e!=o[i-1]==o[i+1]):
  for w in(n^r)*t[a-1:a+2]:w[i-1:i+2]=n,n,n
  for d in-1,1:
   w=i;t[a][i]=e
   while l*(r^o[w:=w+d]):t[a][w]=f
   w=a
   while g*(p[w:=w+d][i]==o[i-1]):t[w][i]=y
 return t