def p(a,n=enumerate):
 for i,f,t,r,u in[(i,f,[r],t[f+3]//r+1,[a[i+1][f+1]])for i,t in n(a)for f,r in n(t)if t[f-1]<r>a[i-1][f]<1]:
  for e in range(-r,r+r+2):n=r*(-1<e<r+2);a[i+e][f-n:f+r+2+n]=t*n+((t,u)[n>0]*(r+2),u+t*n+u)[n>=e>0]+t*n
 return a