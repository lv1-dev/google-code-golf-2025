import re
p=lambda g:exec(r"l=len(g)*3;g[::-1]=zip(*eval(re.sub(r'((.), 0, ([^0]).{%d}\3, \3(.{%d}0)+)'%(l*2,l+4),r'\1+\2',str(g))));"*48)or g