import re
p=lambda g:exec(r"g[::-1]=zip(*eval(re.sub(r'0(?=(.{34}0)+,.(.).{28}\2,.\2)',r'\2',str(g))));"*4)or g