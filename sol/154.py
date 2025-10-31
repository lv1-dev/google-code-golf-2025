import re
p=lambda g:exec(r"g[::-1]=zip(*eval(re.sub('5(.{8}2.{8}|.{5}2.{5})0(?=[^)]*2)',r'0\1 5',str(g))));"*8)or g