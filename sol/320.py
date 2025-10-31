def p(g):
 for c in 1,3,5,7:
  for r in g[2-sum([*zip(*g)][c])>>2:]:r[c]=8
 return g