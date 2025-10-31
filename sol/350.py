import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('(1[, 8]*)0(?=[^])]*1)',r'\1 8',str(g))));"*96)or g