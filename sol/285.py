def p(i):
 n=len(i)
 for a in range(n-1):
  for l in range(n-1):
   for e in range(len({*(r:=i[a][l:l+2]+i[a+1][l:l+2])})&4):
    for o,f in(p:=[(a+(e>1),l+(e&1))]*r[e]):
     for g in range(4):i[a+(e^g>1)+(o-a-(e>1))*(1-2*(g>1))][l+((e^g)&1)+(f-l-(e&1))*(1-2*(g&1))]=r[e^g];p+={(a,l)for a in range(o-1,o+2)for l in range(f-1,f+2)if a<n>l>=i[a][l]^r[e]<1}-{*p}
 return i