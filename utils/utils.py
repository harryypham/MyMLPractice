import math
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

#Fill in the mean and standard deviation of dataset
mean, std = None, None

def unnormalize(imgs, mean, std):
  mean = [-x for x in mean]
  std = [1/x for x in std]
  invTrans = transforms.Compose([ 
      transforms.Normalize(mean = [mean*std for mean, std in zip(mean, std)], std = std),
  ])
  for idx in range(imgs.shape[0]):
    imgs[idx] = invTrans(imgs[idx])
  return imgs


def imshow(img_batch, rows, fig_size):
  img_batch = unnormalize(img_batch, mean, std)
  n_imgs = img_batch.size(0)
  columns = math.ceil(n_imgs/rows)
  plt.figure(figsize=(fig_size * columns / rows, fig_size))
  for i in range(n_imgs):
      img = np.transpose(img_batch[i].numpy(), (1, 2, 0))
      plt.subplot(rows, columns, i+1)
      plt.axis("off")
      plt.imshow(np.clip(img, 0, 1))
  plt.subplots_adjust(hspace=0, wspace=0)
  plt.show()

#To visualize images
# dataiter = iter(trainloader)
# images, labels = next(dataiter)
# imshow(images, rows=2, fig_size=3)