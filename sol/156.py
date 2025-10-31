def p(o):
 f=r=0
 for(k,z,x)in zip(o,o[1:],o[2:]):
  if(h:=sum(z)//4-2)>0<k[l:=z.index(4)+1]*x[l]:f^=k[l]>2;r-=h-2*f*h;z[l:l+h]=[2-f]*h
 return[[f^3*(r>0<f<3)for f in z]for z in o]