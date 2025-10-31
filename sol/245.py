def p(g,e=enumerate):
 R=[(i,j)for(i,r)in e(g)for(j,v)in e(r)if v if v%3*[a:=i-5,b:=j-5]];m,n=map(min,*R)
 for(i,j)in R:g[i][j]-=2;g[i+a-m][j+b-n]+=2
 return g