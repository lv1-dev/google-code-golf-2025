import re
p=lambda g:[g:=[*zip(*eval(re.sub(*c.split(),str(g)))[::-1])]for c in('2..0(?=(..0)+..8) 2,2','2..0..8. 2,7,2,7|',',.7, |8,8,8|')*32][-1]