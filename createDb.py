import cv2, os, numpy as np, progressbar
import constants as cte


listDB = []
bar = progressbar.ProgressBar(len(os.listdir(cte.folderName)))
bar.start()
index = -1
for f in os.listdir(cte.newfoldername):
    os.remove(os.path.join(cte.newfoldername, f))
for filename in os.listdir(cte.folderName):
    index += 1
    f = os.path.join(cte.folderName, filename)
    if os.path.isfile(f):
        img = cv2.imread(f)
        moyPx = np.mean(img, axis=(0,1))
        img = cv2.resize(img, (cte.imgLenDB, cte.imgLenDB))
        cv2.imwrite(os.path.join(cte.newfoldername, str(index)+".bmp"), img)
        listDB.append(moyPx)
    bar.update(bar.currval+1)
bar.finish()
with open("sig.csv", 'w') as of:
    for i in range(len(listDB)):
        of.write("{0}\t{1}\t{2}\t{3}\n".format(i, listDB[i][0], listDB[i][1], listDB[i][2]))