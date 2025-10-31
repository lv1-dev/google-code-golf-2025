import re
p=lambda g:exec("g[:]=eval(re.sub(f'(?<=[24], )[^2](?=(.{{{len(g)*3-1}}})?..[24])','4',str([*zip(*g)])))[::-1];"*96)or g