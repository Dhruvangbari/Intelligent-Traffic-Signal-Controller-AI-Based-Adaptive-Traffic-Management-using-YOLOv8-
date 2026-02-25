import cv2
from detector import detect
from config import VIDEO_SOURCE, LOW_TRAFFIC_TIME, MEDIUM_TRAFFIC_TIME, HIGH_TRAFFIC_TIME

cap = cv2.VideoCapture(VIDEO_SOURCE)

print("Intelligent Traffic Signal Controller Started... Press Q to Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect(frame)
    vehicle_count = len(detections)

    if vehicle_count < 5:
        traffic_level = "LOW"
        green_time = LOW_TRAFFIC_TIME
    elif 5 <= vehicle_count < 15:
        traffic_level = "MEDIUM"
        green_time = MEDIUM_TRAFFIC_TIME
    else:
        traffic_level = "HIGH"
        green_time = HIGH_TRAFFIC_TIME

    cv2.putText(frame, f"Vehicle Count: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Traffic Level: {traffic_level}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    cv2.putText(frame, f"Green Signal Time: {green_time} sec", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("Intelligent Traffic Signal Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
