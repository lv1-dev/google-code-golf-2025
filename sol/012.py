import re
p=lambda g:exec(r"g[::-1]=zip(*eval(re.sub(r'(([^0]).{34}\2, (.), \2, ).(.{31}\2..(.{41})?)0',r'\1\2\4\3',str(g))));"*96)or g