import tobii_g3
import cv2 as cv

tobii = tobii_g3.G3Client("YOUR_DEVICE_ADDRESS")

print(tobii.discover_g3())
tobii.connect()
print(tobii.battery_level)
print(tobii.set_gaze_overlay())
#tobii.open_livestream()

ctr = 0
tobii.send_action("rudimentary","keepalive")
while True: # retrieve the data of IMU and Gaze every sec
    if (ctr < 5):
        print(tobii.gazedataRT)
        print(tobii.imudataRT)
        cv.waitKey(1000)
        ctr +=1
    else:
        tobii.send_action("rudimentary","keepalive")
        ctr=0
#print(tobii.subscribe_signal("rudimentary", "imu"))



# capture images from RTSP video
# cap = cv2.VideoCapture("rtsp://TG03B-080201024101.local:8554/live/all")
# print("cv stream established")
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
