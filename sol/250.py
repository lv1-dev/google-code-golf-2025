import re
p=lambda g:[g:=[*zip(*eval(re.sub(*x,str(g))))][::-1]for x in[("5,([0, ]*)2",r"\1 5,2")]*4+[("5((.{34}0)*)(?=.{34}2)",r"0\1+5")]*4][7]