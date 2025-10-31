g=enumerate
def p(n):z,q,c=zip(*((r,f,n)for r,f in g(n)for f,n in g(f)if n));f=range(e:=z.count(z[-1]));i=e*e;b=z[~i]//e;return[[n[z[0]+b*r][min(q[:-i])+b*f]and c[e*r-i+f]for f in f]for r in f]