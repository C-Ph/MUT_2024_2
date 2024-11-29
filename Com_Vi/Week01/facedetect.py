import numpy as np
import cv2 as cv
import time
import requests
URL_LINE = 'https://notify-api.line.me/api/notify'
LINE_ACCESS_TOKEN = 'ta42fYr16DoGJuQowhIdKLBgDuFdMNM84a8ZnQjU9U9'
LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

def main():
    cascade = cv.CascadeClassifier("haarcascades/haarcascade_frontalcatface.xml")
    nested = cv.CascadeClassifier("haarcascades/haarcascade_frontalcatface.xml")

    #cam = cv.VideoCapture('0')
    cam = cv.VideoCapture('vicat2.mp4')

    while True:
        _ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = time.time()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
        if not nested.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
                file_img = {'imageFile': open('img.png', 'rb')}
                msg = ({'message': 'เจอแมวแล้วววว'})
                LINE_HEADERS = {"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
                session = requests.Session()
                session_post = session.post(URL_LINE, headers=LINE_HEADERS, files=file_img, data=msg)
                cv.imwrite('img' + '.png', vis )
        dt = time.time() - t

        cv.putText(vis,'time: %.1f ms' % (dt*1000),(20, 40),cv.FONT_HERSHEY_SIMPLEX, 2, 255)
        cv.imshow('facedetect', vis)

        if cv.waitKey(5) == 27:
            break

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()