def p(j):
 b=a=sum(j,[0]*10)
 while b[0]%5<1:b=b[1:]
 for r in j:
  l=x=0
  for v in r:r[x],a[x],l=v-5and(v,0,0)or(b[a[x]+l],a[x]+10,l+1);x+=1
 return j