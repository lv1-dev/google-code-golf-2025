def p(g):
 *_,m,r=g;t=s=m.index(r[0])
 while s:s-=1;h=g[s-t-2];h[s]=h[~s]=r[t]
 return g