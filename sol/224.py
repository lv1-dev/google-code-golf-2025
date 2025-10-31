def p(a,E=enumerate):
 (s,*_,t),q=zip(*[(i,j)for i,r in E(a)for j,v in E(r)if(v%5and(k:=v))<v]);r=max(q);q=min(q)+1
 for R in a[s+1:t]:R[q]=R[r-1]=k
 a[s+1][q:r]=R[q:r]=[k]*(r-q);return a