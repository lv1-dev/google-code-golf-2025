def p(a):
 c=a[r:=9].index(k:=sum(a[r]))
 while c<10:
  for y in a:y[c]=k
  if c<9:a[r:=~r][c+1]=5
  c+=2
 return a