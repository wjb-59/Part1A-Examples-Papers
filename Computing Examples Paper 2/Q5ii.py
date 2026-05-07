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
plt.imshow(A, cmap='gray')
print("Image array shape (pixels): {}".format(A.shape))

# Create edge detection filter
G = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
#print(G)

# Create empty matrix to hold convolved values
B = np.zeros(A.shape)

for i in range(1, B.shape[0]-1):
    for j in range(1, B.shape[1]-1):
        for x in range(3):
            for y in range(3):
                B[i, j] += G[x, y]*A[i - 1 + x, j - 1 + y]


plt.figure()
plt.imshow(B, cmap='gray')
plt.show()