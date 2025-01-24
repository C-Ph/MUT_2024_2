import cv2
import matplotlib.pyplot as plt

# อ่านวิดีโอ
image = cv2.VideoCapture('file\OIIAOIIA.mp4')

while True:
    # อ่านเฟรม
    ret, frame = image.read()
    
    if ret:
        # แปลงเป็นภาพขาวดำ
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # ใช้ Canny Edge Detection
        edges = cv2.Canny(gray, threshold1=100, threshold2=200)
        
        # แสดงผลภาพ
        cv2.imshow('Original Video', frame)
        cv2.imshow('Canny Edge Detection', edges)
        
        # กด n เพื่อออกจากโปรแกรม
        if cv2.waitKey(25) & 0xFF == ord('n'):
            break
    else:
        break

# คืนทรัพยากร
image.release()
cv2.destroyAllWindows()
