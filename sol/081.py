import re
p=lambda g:exec("g[::-1]=zip(*eval(re.sub('0(?=, 8.{19}8)','1',str(g))));"*8)or g