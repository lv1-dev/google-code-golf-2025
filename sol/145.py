def p(r,e=len):
 w=e(r[0]);m=[];h=lambda a,f:a|f>=0==r[a][f]and(exec('r[a][f]=%d'%~e(m))or h(a-1,f)-~h(a,f-1));f=w*e(r)
 while f:f-=1;m+=[g:=h(f//w,f%w)]*g
 return[[[2,min(m)//m[~r]*8+m[~r]//max(m)][r<2]for r in r]for r in r]