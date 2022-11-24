import cv2 as cv

cap = cv.VideoCapture('output.avi')
if not cap.isOpened():
    print("Input Camera open failed!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("cap.read() returned nothing!")
        break

    cv.imshow('frame', frame)

    if cv.waitKey(10)==27:
        break

cv.destroyAllWindows()