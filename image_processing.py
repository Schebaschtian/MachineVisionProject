import imageio.v3 as iio
import matplotlib.pyplot as plt 

img = iio.imread("raccon.png")
plt.imshow(img)
plt.axis('off')
plt.show()