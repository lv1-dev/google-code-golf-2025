from itertools import*
p=lambda a,f=lambda a:[*zip(*[map(max,*k)for b,k in groupby(a,max)if b])]:f(f(a))