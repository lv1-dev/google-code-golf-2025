def p(b):
 f=lambda r=0,b=b,i=10:r*(r>14or any(b[r][:i]))or f(r+1,b,i);a=f();p=b.index([0]*10,a);l=b[a:p]
 for w in b'V\\U[,;:':
  n,i=w>>5,w&7;r=10-w%3;o=a-f(i=i);e=f(p)+o;y=[u[:]for u in b]
  while y[e:e+p-a]in([u[:n]*a+u[i-w%3:i]+[0]*(d:=r-n*a)for u in l]for a in(1,2,3)):
   for u in l:y[e][-d:]=([u[i]>7,u[i+1]>7]*4)[:d];e+=1
   e=f(e,y)+o
   if e>o+14:return y