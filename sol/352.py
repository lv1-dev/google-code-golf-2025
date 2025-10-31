import re
p=lambda g:exec("g[:]=zip(*eval(re.sub('0(?=, [12])','1',str(g)))[::-1]);"*4)or g