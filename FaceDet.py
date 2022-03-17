import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # get the video from the camera

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

while True:
    ret, frame = cap.read()  # convert video into images (frames)

    frame = cv2.flip(frame, 1)  # change the direction of frames along the y-axis
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert image to grayscale black and white

    # determine the coordinates of the face in each square
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=1)  # cut the face from image

        text = "Face Detected"
        coordinates = (x + w - 20, y - 20)
        shrift = cv2.FONT_HERSHEY_DUPLEX
        Scale = 1
        color = (0, 0, 255)
        Thickness = 1

        cv2.putText(frame, text, coordinates, shrift, Scale, color, Thickness)

    cv2.imshow('Face Detection', frame)  # display the video

    if cv2.waitKey(2) & 0xFF == ord("q"): # enter 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
