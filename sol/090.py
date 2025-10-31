def p(g):
 _,q,c,w=max((h*(w:=len(k)),q,x%32,w)for x in range(4**8)if(h:=len(q:=g[x>>5&7:x>>8&7]))>1>sum(sum(k:=r[x%32:x>>11])for r in q))
 for r in q:r[c:c+w]=w*[6]
 return g