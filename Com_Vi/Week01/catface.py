import numpy as np
import cv2 as cv
import time
import requests

# Your LINE Notify setup
def send_to_line(image_path):
    URL_LINE = 'https://notify-api.line.me/api/notify'
    LINE_ACCESS_TOKEN = 'ta42fYr16DoGJuQowhIdKLBgDuFdMNM84a8ZnQjU9U9'  # Use environment variable for security
    LINE_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', "Authorization": "Bearer " + LINE_ACCESS_TOKEN}

    try:
        # Send image to LINE
        with open(image_path, 'rb') as file_img:
            msg = {'message': 'พบเจ้าเหมียว'}
            session = requests.Session()
            session_post = session.post(URL_LINE, headers=LINE_HEADERS, files={'imageFile': file_img}, data=msg)
            print("ภาพถูกส่งไปยัง LINE แล้ว")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการส่งภาพ: {e}")

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

    cam = cv.VideoCapture('/COD_E/001_Project/CLASS/Lab1/vicat2.mp4')

    while True:
        _ret, img = cam.read()
        if not _ret:
            print("Failed to read frame.")
            break

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = time.time()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))

        if len(rects) > 0:  # Only proceed if faces are detected
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))

            # Save the image as img.png
            cv.imwrite('img.png', vis)

            # Send the image to LINE
            send_to_line('img.png')

        dt = time.time() - t
        cv.putText(vis, 'time: %.1f ms' % (dt*1000), (20, 40), cv.FONT_HERSHEY_SIMPLEX, 2, 255)
        cv.imshow('facedetect', vis)

        if cv.waitKey(5) == 27:  # Press 'Esc' to exit
            break

    print('Done')
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
