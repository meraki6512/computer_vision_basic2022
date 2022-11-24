import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Input Camera open failed!")
    exit()

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)
out = cv.VideoWriter('output.avi', fourcc, fps, (w,h), 0)


if not out.isOpened():
    print('Output File open failed!')
    exit()

ret, frame = cap.read()
inv = False
count = fps*3

while cv.waitKey(delay) != 27:
    prev_frame = frame
    ret, frame = cap.read()
    if not ret:
        break
    cur = np.mean(frame)
    prev = np.mean(prev_frame)

    if (np.abs(cur-prev) >= 30):
        inv = True

    if inv:
        count -= 1
        frame = ~frame
        if (count <= 0):
            inv = False

    out.write(cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
    cv.imshow('frame', frame)

cap.release()
out.release()
cv.destroyAllWindows()

