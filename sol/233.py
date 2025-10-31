def p(a):
 l={},{};r=range(9)
 for f in range(len(a)-2):
  for p in range(len(a[0])-2):
   if(n:=[a[f+t//3][p+t%3]for t in r])and(m:={*n}-{2})and min(m)and(n:=(*(p==2for p in n),)):
    for t in range(4):l[t>0][n]=m;n=n[2::3]+n[1::3]+n[::3]
    for t in r:a[f+t//3][p+t%3]=0
 for t in range(2):a[:]=map(list,zip(*filter(any,a)))
 for l in l:
  for f in range(len(a)-2):
   for p in range(len(a[0])-2):
    if(n:=[a[f+t//3][p+t%3]for t in r])and(m:=l.get(n:=(*(p<1for p in n),)))and(m:=m.pop()):
     for t in r:a[f+t//3][p+t%3]=n[t]*2 or m
 return a