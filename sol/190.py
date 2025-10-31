import re
p=lambda g:exec(r"g[::-1]=zip(*eval(re.sub(r'0(?=(.{31}0, ([^0])){2})',r'\2',str(g))));"*20)or g