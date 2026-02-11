import cv2;
import pygame;

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")

cap = cv2.VideoCapture(0);

eyes_closed_frames = 0
threshold = 15
audio_playing = False

while True:
    ret, frame = cap.read();
    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.2,5,minSize=(80,80))

    for (x, y, w, h) in faces:
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_gray,1.3,5)

        if(len(eyes) == 0):
            eyes_closed_frames += 1
            label = "Eyes Closed"
        else:
            eyes_closed_frames = 0
            label = "Eyes Open"

        for(sx, sy, sw, sh) in eyes:
            cv2.rectangle(face_color, (sx,sy), (sx+sw,sy+sh),(0,255,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    if eyes_closed_frames > threshold and not audio_playing:
        pygame.mixer.music.play()
        audio_playing = True
    
    if eyes_closed_frames == 0 and audio_playing:
        pygame.mixer.music.stop()
        audio_playing =False

    cv2.imshow("Sleep Detector",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
