def p(a):
 r=[[5]*9for k in range(9)]
 for d in range(len(a)-2):
  for t in range(len(a[0])-2):
   e=0
   for k in range(9):
    b=a[d+k//3][t+k%3]
    if b<1:break
    if b-5:e+=1<<k
   else:
    i=1-(e&7>0)+(e>>6&7>0)
    b=1-(e&73>0)+(e>>2&73>0)
    for k in range(9):
     if e&1<<k:r[i*3+k//3][b*3+k%3]=a[d+k//3][t+k%3]
 return r