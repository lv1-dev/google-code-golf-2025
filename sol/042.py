s=range
def p(i):
 for t in s(81):
  if f:=4>i[r:=t//9][c:=t%9]>i[r-1][c]|i[r][c-1]:
   while(d:=i[r+f])[c]:f+=1
   for t in s((e:=(d[c+f]%2-d[c-f]%2)*f)*e*2):
    if(n:=r+f+t//f-2*f*(d:=t<f*f))<10>(d:=c+t%f+3*e*d-e)>-1<n:i[n][d]=8
 return i