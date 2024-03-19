import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use OpenCV to detect QR codes
    decoded_objects = decode(gray)

    # If QR codes are detected, return their data
    if decoded_objects:
        for obj in decoded_objects:
            print("Data:", obj.data.decode())
    else:
        print("No QR code detected")

# Capture video from the Raspberry Pi camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('frame', frame)

    # Check for QR codes in the frame
    read_qr_code(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


