import cv2
import matplotlib.pyplot as plt
from numpy import arange
from decimal import Decimal

pictures_dir = 'C:\\Users\\Wangqian Miao\\Desktop\\1\\'
imgs = []

for i in arange(0.0000,0.0225, 0.0025):
    Mz = Decimal(i).quantize(Decimal('0.0000'))
    for j in arange(0.002, 0.011, 0.001):
        Kappa = Decimal(j).quantize(Decimal('0.000'))
        picname = pictures_dir + 'Mz' + str(Mz) + 'Kappa' + str(Kappa) + 'Order0Scale1.0.png'
        #print(picname)
        img = cv2.imread(picname, cv2.IMREAD_UNCHANGED)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgs.append(img)

conf = ['331','332','333','334','335','336','337','338','339']

Mzs = [i for i in arange(0.0000,0.0225, 0.0025)]

index = 0
print(len(imgs))
for i in range(len(imgs)):
    if(i%9 == 0):
        fig = plt.figure(facecolor='white')
        plt.gca().xaxis.set_major_locator(plt.NullLocator()) 
        plt.gca().yaxis.set_major_locator(plt.NullLocator()) 
        plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)
        fig.set_size_inches(18.5, 10.5)

        for j in range(9):
            plt.subplot(conf[j])
            plt.imshow(imgs[i+j])
            plt.axis('off')
        plt.suptitle('Mz = ' + str(Decimal(Mzs[index]).quantize(Decimal('0.0000')))+', Kappa from 0.002 to 0.010, step 0.001')
        plt.savefig('C:\\Users\\Wangqian Miao\\Desktop\\scale1\\'+str(i)+'.png', dpi =500)
        index = index + 1





