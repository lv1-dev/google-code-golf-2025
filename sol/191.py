def p(m):
 f=len(m);r=bytes(sum(m,[]));b,p=divmod(r.find(1),f);n,e=divmod(r.rfind(1),f);r=[[e>3for e in r[p+1:e]]for r in m[b+1:n]]
 for i in range(4):
  for r in r,[[*r]for r in zip(*r)]:r=r[::-1];b,n=len(r),len(r[0]);[exec('m[e][d]=1')for i in range(f)for p in range(f)if r==[[e>3for e in r[p:p+n]]for r in m[i:i+b]] for e in range(i-1,i+b+1)for d in range(p-1,p+n+1)if f>e>-1<d<f>4>m[e][d]]
 return m