def p(g,k=0):
 f=sum(g,[]);x=f.index
 for v in f:g[k//10][k%10]-=v;g[(k+x(1)-x(v or 1))//10][k%10]+=v;k+=1
 return g