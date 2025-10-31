def p(b):
 for t in[1]*4:
  for u,a in enumerate(b):
   if~(f:=bytes(a).find(b'\0')):
    while a[f-t]:t+=1
    for a in b[u-t+1:u+t]:a[f:]=[a[f]]*(len(a)-f)
  b[::-1]=map(list,zip(*b))
 return b