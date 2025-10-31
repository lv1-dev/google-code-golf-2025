def p(d):
 def l(f,u):
  if len(d)>f>-1<u<len(d[0])and(a:=d[f][u]):n[a]=n.get(a,[])+[(f,u)];d[f][u]=0;l(f+1,u);l(f-1,u);l(f,u+1);l(f,u-1)
 r=[n for f in range(len(d))for u in range(len(d[0]))if(n:={},l(f,u))[0]]
 a,={*r[0]}&{*r[1]}
 for n in r:
  if len(n[a])<len(n[sum(n)-a]):e,i=n[a][0];l=n[sum(n)-a]
 for n in r:
  s=int(len(n[a])**.5);g=sum(n)-a
  for f,u in n[a]:
   d[f][u]=a
   for r,n in l:d[f+s*(r-e)][u+s*(n-i)]=g
 return d