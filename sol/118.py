def p(r):
 a={(l,n)for l in range(len(r))for n in range(len(r[0]))if r[l][n]&2};d=lambda e,l:[e and(d(e[1:],l)or not e[0]&l and d(e[1:],l|e[0])),l][a<=l]
 for n in 2,3:
  l=[l for d in range(len(r))for e in range(len(r[0]))for l in[{(l,n)for l in range(-n,n+1)for l,n in[(d+l,e),(d,e+l)]if len(r)>l>-1<n<len(r[0])}]if min(r[l][n]for l,n in l)&2]
  if l:=d(l,set()):
   for l,n in l:r[l][n]+=3*(r[l][n]&1)
   return r