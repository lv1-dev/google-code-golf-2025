import re
p=lambda g:[g:=[*zip(*eval(re.sub(*x.split(),str(g))))][::-1]for x in['(?<=[^0],.)0(?=[^])]*[1-9]) 8']*96+['0,.8 0,0']*4][-1]