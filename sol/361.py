r=range
def p(a):
 [(i:=f+x+t,d:=x-f)for t in(2,3)for x in r(8)for f in r(8)if min(min(x[f:f+t])for x in a[x:x+t])]
 for f in r(100):n=a[x:=f//10][f:=f%10];n and exec('x,f=d+f,i+~x;a[x][f]=n;'*3)
 return a