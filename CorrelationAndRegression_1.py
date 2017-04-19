x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3 ]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
n = len(x);
sx = sum(x)
sy = sum(y)
xb = sx/n
yb = sy/n
xa1 = [t - xb for t in x]
ya1 = [t - yb for t in y]
xa2 = [t*t for t in xa1]
ya2 = [t*t for t in ya1]
numer = sum([u*v for u,v in zip(xa1, ya1)])
denom = ((sum(xa2))**(1/2.0))*((sum(ya2))**(1/2.0))
print('{0:.3f}'.format(numer/denom))