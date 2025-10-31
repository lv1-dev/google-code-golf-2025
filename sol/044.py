def p(p):
 p=sum(p,[]);t=[1]*100;f,r={},{}
 for a,i in enumerate(p):
  if t[a]:
   t[a]=0;n=[a];u=i<1;e=0
   for a in n:
    e+=1<<a
    for a in a-1,a+1,a-10,a+10:
     if -1<a<100:
      if i-p[a]:u*=p[a]==5
      elif t[a]:n+=a,;t[a]=0
   e//=e&-e;f[e*u-i]=n;r[i]=e
 for i in r:
  if n:=i%5and f.pop(r[i],0):
   for a in n:p[a]=i
   for a in f[-i]:p[a]=0
 return[*zip(*[iter(p)]*10)]