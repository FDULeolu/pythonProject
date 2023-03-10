import gzip
import os

import torch
import torchvision
import numpy as np
from torchvision import datasets, transforms
#from Pillow import Image
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, Dataset

# 导入MNIST数据集
train_data = datasets.MNIST(
             root="./data/",
             train=True,
             transform=transforms.ToTensor(),
             download=True)

test_data = datasets.MNIST(
            root='./data/',
            train=False,
            transform=transforms.ToTensor(),
            download=True)

# 加载数据集
train_data_loader = torch.utils.data.DataLoader(
            dataset=train_data,
            batch_size=64,
            shuffle=True,
            drop_last=True)

test_data_loader = torch.utils.data.DataLoader(
            dataset=test_data,
            batch_size=64,
            shuffle=False,
            drop_last=False)


# 预览
images, labels = next(iter(train_data_loader))

img = torchvision.utils.make_grid(images)

img = img.numpy().transpose(1,2,0)
std = [0.5,0.5,0.5]
mean = [0.5,0.5,0.5]
img = img * std + mean
print(labels)
plt.imshow(img)
plt.show()

# images：Tensor(64,1,28,28)、labels：Tensor(64,)
images, labels = next(iter(train_data_loader))  #(1,28,28)表示该图像的 height、width、color(颜色通道，即单通道)
images = images.reshape(64, 28, 28)
img = images[0, :, :]	# 取batch_size中的第一张图像
np.savetxt('img.txt', img.cpu().numpy(), fmt="%f", encoding='UTF-8')	# 将像素值写入txt文件，以便查看
img = img.cpu().numpy()	#转为numpy类型，方便有效输出

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111)
ax.imshow(img, cmap='gray')
width, height = img.shape
thresh = img.max()/2.5

for x in range(width):
    for y in range(height):
        val = round(img[x][y], 2) if img[x][y] !=0 else 0
        ax.annotate(str(val), xy=(y, x),
                    horizontalalignment='center',
                    verticalalignment='center',
                    color='white' if img[x][y] < thresh else 'black')
plt.show()
