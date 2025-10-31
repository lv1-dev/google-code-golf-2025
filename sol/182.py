def p(d,r=0):
 s=sum(d,[]);e=lambda r:[t for t in range(25)if s[r+20*(t//5)+t%5]]
 while s[r]*s[r+120]-25|(o:=s[r+63])<2:r+=1
 f=e(r+21)
 for r in range(256):
  for t in(e(r+r//16*4)==f)*f:d[r//16+t//5][r%16+t%5]=o
 return d