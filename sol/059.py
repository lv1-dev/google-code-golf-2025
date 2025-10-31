def p(g,R=range(11)):
 s=[0]*9;z=0
 for v in sum(g,[]):
  if v%5:s[z//44*3+z%11//4]+=1;k=v
  z+=1
 return[[5-(5-k*(s[i//4*3+j//4]==max(s)))*(i&3<3>j&3)for j in R]for i in R]