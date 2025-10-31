def p(a,n=1):
 for c in(f:=range(11-n)):
  for l in f:
   for r in(r:=a[c+1:c-~n])*all(a[c][l:(o:=l+n+2)]+a[c-~n][l:o]+[c[l:o]==[5,*[0]*n,5]for c in r]):r[l+1:o-1]=n*[2]
 n>3or p(a,n+1);return a