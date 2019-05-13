from pylab import plot, imshow, show
from numpy import loadtxt, array, zeros, sqrt, pi

pix = 500
size = 100. # cm 
step = size / pix # cm/pixel
lda = 5.0 # cm
k = 2.*pi / lda
zeta0 = 1.0 # cm
x1 = 50. # cm
y1 = 50. # cm

x = zeros(pix, float)
y = zeros(pix, float)

for i in range(pix):
    x[i] = step*i
    y[i] = step*i
    
outfile = open("outdata.dat", "w")

for xx in range( len(x) ):
    for yy in range( len(y) ):
        r = sqrt()
        outfile.write("%0.1f " % (sqrt( (x1-x[xx])*(x1-x[xx]) + (y1-y[yy])*(y1-y[yy]) ) ) )
    
    outfile.write("\n")
    
outfile.close()

data = loadtxt("outdata.dat", float)
imshow(data)
show()
