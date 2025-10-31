import re
p=lambda g:exec("g[::-1]=zip(*eval(re.sub('0(?=, 8, 8)|(?<=5, )0(?=[^])]*5)','8',str(g))));"*28)or g