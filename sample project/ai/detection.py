from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        results = model(frame)

        annotated = results[0].plot()

        cv2.imshow("Detection", annotated)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()