def p(g):
 for n in range(1080):k=g[i:=n//19%19][j:=n%19];g[~j][i]|=k;g[i][j+2*(i<j<16-i)]|=k
 return g