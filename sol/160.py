R=range
def p(a):
 for n in R(64):
  for k in R(sum(a[n//8+i//3][n%8+i%3]&1for i in R(9))//8*9):a[n//8+k//3][n%8+k%3]=372>>k&2
 return a