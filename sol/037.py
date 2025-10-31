import re
p=lambda g:exec(r'g[::-1]=zip(*eval(re.sub(r"(([^0]).{34})0(?=(.{35})*.{34}\2)",r"\1\2",str(g))));'*96)or g