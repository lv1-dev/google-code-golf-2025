s=lambda p:[*map(list,zip(*p))]
def a(p):
 b=s(p);a=0;r,a=max((a:=(b[i].count(0)>25)*-~a,i)for i in range(30))
 for i in range(30):
  for a,u in(a-r+2,a),(0,a),(a,30):
   if sum(sum(s(b[a:-~u])[i and i-1:i+2],[]))<1:p[i][a:u]=[3]*(u-a)
 return r
p=lambda p:(a(r:=s(p))>a(p))*s(r)or p