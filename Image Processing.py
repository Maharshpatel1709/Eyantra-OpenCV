import numpy as np
import cv2
import csv

bird = cv2.imread('bird.jpg', 1)
cat = cv2.imread('cat.jpg', 1)
flowers = cv2.imread('flowers.jpg', 1)
horse = cv2.imread('horse.jpg', 1)

bh = (bird.shape[0])
bw = (bird.shape[1])
ch = (cat.shape[0])
cw = (cat.shape[1])
fh = (flowers.shape[0])
fw = (flowers.shape[1])
hh = (horse.shape[0])
hw = (horse.shape[1])

# Task A

with open('stats.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["bird.jpg", str(bh), str(bw), str(bird.shape[2]), str(bird[bh//2, bw//2][0]), str(bird[bh//2, bw//2][1]), str(bird[bh//2, bw//2][2])])
    writer.writerow(["cat.jpg", str(ch), str(cw), str(cat.shape[2]), str(cat[ch // 2, cw // 2][0]), str(cat[ch // 2, cw // 2][1]), str(cat[ch // 2, cw // 2][2])])
    writer.writerow(["flowers.jpg", str(fh), str(fw), str(flowers.shape[2]), str(flowers[fh // 2, fw // 2][0]), str(flowers[fh // 2, fw // 2][1]), str(flowers[fh // 2, fw // 2][2])])
    writer.writerow(["horse.jpg", str(hh), str(hw), str(horse.shape[2]), str(horse[hh // 2, hw // 2][0]), str(horse[hh // 2, hw // 2][1]), str(horse[hh // 2, hw // 2][2])])


# Task B

for i in range(ch):
    for j in range(cw):
        cat[i, j][0] = 0
        cat[i, j][1] = 0

cv2.imwrite("cat_red.jpg", cat)


# Task C

flowers = cv2.cvtColor(flowers, cv2.COLOR_BGR2BGRA)

for i in range(fh):
    for j in range(fw):
        flowers[i, j][3] *= 0.5

cv2.imwrite('flowers_alpha.png', flowers)


# Task D

Intensity = np.zeros((hh, hw))

for i in range(hh):
    for j in range(hw):
        Intensity[i][j] = (0.11 * horse[i, j][0]) + (0.59 * horse[i, j][1]) + (0.3 * horse[i, j][2])

print(Intensity)

horse = cv2.cvtColor(horse, cv2.COLOR_BGR2GRAY)

cv2.imwrite('horse_gray.jpg', horse)
