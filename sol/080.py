def p(o):
 i=len(o);g=1
 while o[g]==o[0]:g+=1
 e=g+1
 n=next((o[r][f],o[r-e][f],o[r-e][f-e])for r in range(e,i,e)for f in range(e,i,e)if o[r][f]!=o[r-e][f]==o[r][f-e]>0)
 for r in range(0,i,e):
  for f in range(0,i,e):
   if o[r][f]==n[0]:
    for h in(-e,0,e):
     for e in(-e,0,e):
      if r+h>-1<f+e<i:
       for p in o[r+h:][:g]:p[f+e:f+e+g]=[n[(h!=0)+(e!=0)]]*g
 return o