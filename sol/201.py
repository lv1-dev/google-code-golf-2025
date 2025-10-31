def p(e):
 (u,d),*r,(f,t)=((n,r)for n,e in enumerate(e)for r,i in enumerate(e)if i==4);o,r,i=min((n,r,i)for n,e in enumerate(e)for r,i in enumerate(e)if i>0>n-u|f-n|r-d|t-r);n=min(r for n,e in enumerate(e)for r,i in enumerate(e)if i>0>n-u|f-n|r-d|t-r)
 for r in e[u+1:f]:r[d+1:t]=e[o][n:n+t-d-1][::i==e[u+1][d]or-1];o+=1
 return[r[d:t+1]for r in e[u:f+1]]