import cv2

cap = cv2.VideoCapture('RoseBloom.mp4')
flag = 0

while cap.isOpened():
    ret, frame = cap.read()
    flag += 1
    if ret == True:

        cv2.imshow('Video', frame)

        if flag == 150:
            cv2.imwrite('frame_as_6.jpg', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

rose = cv2.imread('frame_as_6.jpg', 1)

rose[:, :, 0] = 0
rose[:, :, 1] = 0

cv2.imwrite('frame_as_6_red.jpg', rose)




