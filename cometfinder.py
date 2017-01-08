import scipy
import scipy.misc
import scipy.ndimage.measurements
from scipy.ndimage import label
import matplotlib.pyplot as plt
import numpy as np

image1 = scipy.misc.imread('img/20170107_2136_c2_1024.jpg', flatten=1)
image2 = scipy.misc.imread('img/20170107_2148_c2_1024.jpg', flatten=1)
image4 = scipy.misc.imread('img/20170107_2212_c2_1024.jpg', flatten=1)
image3 = scipy.misc.imread('img/20170107_2200_c2_1024.jpg', flatten=1)

thold = 12

diff1 = np.subtract(image1, image2)
diff2 = np.subtract(image4, image3)
diff = np.subtract(diff1, diff2)

x1 = 000
x2 = 512
y1 = 512
y2 = 1024

x = diff[y1:y2,x1:x2].astype(int)

xt = np.where(x<-thold, x,0)
d1 = np.where(xt==0, xt,-1)
l1, n1 = label(d1, scipy.ones((3,3)))

xt = np.where(x>thold, x,0)
d2 = np.where(xt==0, xt,1)
l2, n2 = label(d2, scipy.ones((3,3)))

xt = np.where(x<-thold, x,0)
d3 = np.where(xt==0, xt,-1)
l3, n3 = label(d3, scipy.ones((3,3)))

xt = np.where(x>thold, x,0)
d4 = np.where(xt==0, xt,1)
l4, n4 = label(d4, scipy.ones((3,3)))

pairs = list()

centres1 = scipy.ndimage.measurements.center_of_mass(d1, l1, range(1, n1+1))
centres2 = scipy.ndimage.measurements.center_of_mass(d2, l2, range(1, n2+1))
centres3 = scipy.ndimage.measurements.center_of_mass(d3, l3, range(1, n3+1))
centres4 = scipy.ndimage.measurements.center_of_mass(d4, l4, range(1, n4+1))

#for c1 in centres1:
#	for c2 in centres2:
#		for c3 in centres3:
#			for c4 in centres4:
#				if (c1[0]-c2[0]-c3[0]-c4[0])**2 + (c1[1]-c2[1]-c3[1]-c4[1])**2 < 12*12:
#					pairs.append((c1,c2,c3,c4))

#print len(pairs)

imgplt = plt.imshow(d1+d2+d3+d4)
imgplt.set_cmap('bwr')

plt.show()
