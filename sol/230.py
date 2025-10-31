import re
p=lambda g:[g:=[*zip(*eval(re.sub('0(?=, 0.{%d}0, 5)'%(len(g)*3-2),c,f'{g}')))][::-1]for c in'1243'][3]