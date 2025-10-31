def p(i):
 e=[(a,o,n)for a,n in enumerate(i)for o,n in enumerate(n)if n&1]
 for d,u,n in e:
  if n==2:a,o=d,u
  e+=[(a,o,n)for a,n in enumerate(i)for o,n in enumerate(n)if n*(2>d-a>-2<u-o<2)and(a,o,n)not in e]
 e=[(d-a,u-o,n)for d,u,n in e]
 for l in(1,-1)*4:
  for a,o,n in[(a,o,n)for a,n in enumerate(i)for o,n in enumerate(n)if n==2<all(len(i)>a+d>-1<o+u*l<len(i[0])and i[a+d][o+u*l]^n<4 for d,u,n in e)+2]:
   for d,u,n in e:i[a+d][o+u*l]|=n
  if l+1:e=[(u,-d,n)for d,u,n in e]
 return i