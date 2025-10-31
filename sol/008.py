import re
p=lambda g:exec(r"g[:]=zip(*eval(re.sub('(\(.*2[^(]*)(.*?)(?=\([^)]*8)',r'\2\1',str(g)))[::-1]);"*8)or g