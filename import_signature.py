from skimage.morphology import skeletonize
from skimage import draw
import numpy as np
import matplotlib.pyplot as plt

signature = plt.imread("resources/signature2.png")
plt.imshow(signature)
