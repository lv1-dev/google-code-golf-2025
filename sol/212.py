def p(a,b=1,k=99):
 v=a[i:=k//10][j:=k%10]
 while~i%11*v>0<a[i][j]^5:a[i][j]=v;i-=b^v&1or-1
 if k:p(a,5*b>v,k-1);return a