def p(a):
 s,k={x:0for x in sum(a,[])[::-1]if x};j=0
 for c in zip(*a):
  for r in a[(m:=bytes(c).rfind(k)%20+1):]*sum(c[m:]):r[j]=s
  j+=1
 return a