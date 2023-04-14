import cv2, numpy as np, os, matplotlib.pyplot as plt, progressbar
import constants as cte

file="doc/jactat.jpg"
img = cv2.imread(file)
#img = cv2.resize(img, (256, 256))


n, m, _ = np.shape(img)
finalImg = np.zeros((cte.imgLenDB*n, cte.imgLenDB*m, 3), dtype=np.uint64)

imgSig = []

with open("sig.csv") as of:
    sig = of.readlines()
    for x in sig:
        tab = (x.replace('\n',"").split("\t")[1:])
        imgSig.append(np.uint8(np.asarray(tab, dtype=float)))
imgSig = np.array(imgSig, dtype=np.int16)
img = np.array(img, dtype=np.int16)
bar = progressbar.ProgressBar(n*m)
bar.start()
k=0
for i in range(n):
    for j in range(m):
        entreDeux = np.asarray(imgSig - img[i][j], dtype=np.int32)
        mini = np.argmin(np.linalg.norm(entreDeux, axis=1), axis=0)
        pixelImg = cv2.imread(os.path.join(cte.newfoldername, "{0}.bmp".format(mini)))
        finalImg[i*cte.imgLenDB:(i+1)*cte.imgLenDB, j*cte.imgLenDB:(j+1)*cte.imgLenDB] = pixelImg
        k+=1
        bar.update(k)
np.asarray(finalImg, dtype=np.uint8)
cv2.imwrite(os.path.join(os.getcwd(), cte.modifiedName),finalImg)
plt.axis("off")
plt.imshow(finalImg)
plt.show()
bar.finish()