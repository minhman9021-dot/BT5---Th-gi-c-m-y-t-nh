import cv2
import numpy as np
from tkinter import Tk, filedialog

# Nạp bộ nhận diện khuôn mặt có sẵn của OpenCV
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

if face_cascade.empty():
    print('Khong nap duoc file cascade')
    exit()

count = 0  # đếm số ảnh mặt đã lưu, tránh bị ghi đè


def save_face(frame, faces):
    global count
    for (x, y, w, h) in faces:
        count += 1
        crop = frame[y:y+h, x:x+w]
        cv2.imwrite("file{}.png".format(count), crop)
    print('Da luu, tong so anh:', count)


# Hộp thoại chọn video
root = Tk()
root.withdraw()
root.attributes('-topmost', True)
video_path = filedialog.askopenfilename(
    title='Chon video',
    filetypes=[('Video', '*.mp4 *.avi *.mov *.mkv'), ('Tat ca', '*.*')])
root.destroy()

if not video_path:
    print('Ban chua chon video')
    exit()

camera = cv2.VideoCapture(video_path)
if not camera.isOpened():
    print('Khong mo duoc video')
    exit()

while True:
    ret, img = camera.read()
    if not ret:          # hết video thì dừng
        break

    # chuyển img thành xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 10, minSize=(30, 30))

    # xử lý phím TRƯỚC khi vẽ khung, để ảnh lưu không dính viền xanh
    key = cv2.waitKey(30)
    if key == ord('q'):
        break
    elif key == ord('s'):
        save_face(img, faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("video", img)

camera.release()
cv2.destroyAllWindows()