import re
def p(i):
 r=re.sub(', ','',str(i+[*zip(*i)]));u=r+r[::-1];i=int(max(r,key=r.count));a={0:(0,i)}
 for r in range(10):
  if(r^i)*(t:=re.findall(f'{r}+',u)):e=len(re.findall(f'{r}{r}([^]){r}]+){r}|$',u)[0]);a[len(max(t))*(1+(e>0))+e>>1]=-~e>>1,r
 r=max(a)
 return[[i*((g:=a[max(abs(r),abs(t))])[0]>min(abs(r),abs(t)))or g[1]for r in range(-r,r+1)]for t in range(-r,r+1)]