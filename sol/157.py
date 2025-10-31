def p(p):
 a=sum(p,e:=[]);p=[];n=[[]];r=15
 for i in range(16):
  if(5in a[i::r])*r>i:p+=[i]
  elif p:i=[n for n in range(150)if a[n]>4and n%r in p];e+=[[n-i[0]for n in i]];p=[];n=[i+[n]for i in n for n in range(45)if 1>a[n]]
 for i in n:
  if all((i:=[any(n-i in e*(6>i%r-n%r)for i,e in zip(i,e))|a[n]%5for n in range(150)])[:45])*3>max(i):return[i[n*r:][:r]for n in range(10)]