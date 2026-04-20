import numpy as np
import matplotlib.pyplot as plt
import urllib
import PIL
from IPython.display import display


urllib.request.urlretrieve("https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/main/images/southwing.png", 
                           "baker.png")
A = PIL.Image.open("baker.png")
display(A)

A = np.asarray(A)
plt.imshow(A, cmap='gray');
print("Image array shape (pixels): {}".format(A.shape))

# Create edge detection filter
G = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
#print(G)

# Create empty matrix to hold convolved values
B = np.zeros_like(A)

d = G.shape[0]//2

for i in range(B.shape[0]-1):
    for j in range(B.shape[1]-1):
        for k in range(3):
            for l in range(3):
                B[i, j] += G[k, l]*A[i-d+k, j-d+l]

plt.imshow(B, cmap='gray');