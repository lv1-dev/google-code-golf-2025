f=lambda g,k=0:[[max(c,k:=k^(3<~sum(r)&c)*3)for c in r]for r in zip(*g)]
p=lambda g:f(f(g))