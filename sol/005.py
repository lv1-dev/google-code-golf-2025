def p(p):
 r=max(([(h+e,f+g)for e in range(3)for g in range(3)if p[h+e][f+g]]for h in range(19)for f in range(19)),key=len)
 for e in(-4,0,4):
  for g in(-4,0,4):
   o=max((e or g)and p[h+e][f+g]for h,f in r)
   for h,f in r:
    while o and 0<=(h:=h+e)<21 and 0<=(f:=f+g)<21:p[h][f]=o
 return p