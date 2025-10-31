import re
p=lambda g:exec(r"g[::-1]=zip(*eval(re.sub('0(.{8}2.{8}|.{5}2.{5})5(?=[^)]*2)',r'5\1 0',str(g))));"*8)or g