import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

video = cv2.VideoCapture('ot.mp4')

size = (int(video.get(3)),int(video.get(4)))

output_od = cv2.VideoWriter('output_ot.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

while video.isOpened():
    ret,frame = video.read()
    if ret==True:
        bbox,labels,conf = cv.detect_common_objects(frame)
        j=0
        for i in bbox:
            x1,y1,x2,y2 = i[0],i[1],i[2],i[3]
            cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)
            cv2.putText(frame, labels[j]+" "+str("{:.2f}".format(conf[j])), (x1,y1+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1, cv2.LINE_AA)
            j+=1
#         frame = draw_bbox(frame, bbox, labels, conf)
        output_od.write(frame)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

video.release()
output_od.release()
cv2.destroyAllWindows()