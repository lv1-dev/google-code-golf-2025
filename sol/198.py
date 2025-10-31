import re
p=lambda g:exec("g[::-1]=zip(*eval(re.sub('%s',str(g))));"*3%("0','3",f"3(?=.{{{len(g)*3-2}}}3, [^3], 3)','4","4,.3','4,4")*96)or g