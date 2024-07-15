import requests
import cv2
import numpy as np

url = "http://192.168.0.6:8080/shot.jpg"

try:
    while True:
        cam = requests.get(url, timeout=5)  # Timeout after 5 seconds if no response
        if cam.status_code == 200:
            imgNp = np.array(bytearray(cam.content), dtype=np.uint8)
            img = cv2.imdecode(imgNp, -1)
            cv2.imshow("cam", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except requests.exceptions.RequestException as e:
    print(f"Error fetching image: {e}")

except cv2.error as e:
    print(f"OpenCV error: {e}")

finally:
    cv2.destroyAllWindows()
