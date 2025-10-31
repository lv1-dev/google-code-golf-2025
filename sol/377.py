f=lambda g:[g:=r for r in zip(*g)if g!=r]
p=lambda g:f(f(g))