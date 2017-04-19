x = [15., 12., 8., 8., 7., 7., 7., 6., 5., 3. ]
y = [10., 25., 17., 11., 13., 17., 20., 13., 9., 15.]
n = len(x)
sx = sum(x)
sy = sum(y)
x2 = [a*a for a in x]
y2 = [b*b for b in y]
sx2 = sum(x2)
sy2 = sum(y2)
xy = [a*b for a,b in zip(x,y)]
sxy = sum(xy)
numera = sy*sx2 - sx*sxy
denoma = n*sx2 - sx*sx
numerb = n*sxy - sx*sy
denomb = n*sx2 - sx*sx
print('{0:.1f}'.format(10*(numerb/denomb)+(numera/denoma)))