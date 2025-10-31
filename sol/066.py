n=lambda d:[*map(list,zip(*d))]
def p(r):
 for e in 1,-1:
  for s in 1,-1:
   for z in range(2):
    m=[a[::e]for a in r[::s]]
    m=(m,n(m))[z]
    i=sum(m,[]).index
    x=len(m)
    d,p=divmod(i(2),x)
    i,l=divmod(i(3),x)
    for f in range(d,x-1):
     if m[f][o:=p+1]&m[f-(a:=i>f or-1)][l]^8|sum(m[f][l:o]+n(m)[p][d+2:f]+sum(m[f+a:i-a//2:a],[])[l::x],p<l)<1:
      for a in m[f+a:i-a//2:a]:a[l]=3
      for a in m[d+2:f]:a[p]=3
      m[f][l:o]=[3]*(o-l);return[a[::e]for a in(m,n(m))[z]][::s]