def p(p):
 f=len(p[0]);l=sum(p,[]);n,e=a=[[],[]];r=[l.index(1)]
 for d in r:
  if l[d:d+1]>[0]:
   a[l[d]-1]+=d,;l[d]=0;r+=d-f,d+f,d-(d%f>0),d+(d%f<f-1)
 i=min(e);r={(d//f,d%f)for d in range(len(l))if l[d]}
 while r:
  a,l=min(r);o=3
  while{(a+(d//f-i//f)*o+u//o,l+(d%f-i%f)*o+u%o)for u in range(o*o)for d in e}-r:o-=1
  r-={(a+(d//f-i//f)*o+u//o,l+(d%f-i%f)*o+u%o)for u in range(o*o)for d in e}
  for a,l in {(a+(d//f-i//f)*o+u//o,l+(d%f-i%f)*o+u%o)for u in range(o*o)for d in n}:p[a][l]+=l>=0
 return p