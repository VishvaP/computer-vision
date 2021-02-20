import cv2
cap = cv2.VideoCapture('Vishva Patel Intro.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('slow_motion.avi', fourcc, 5, (640,  480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("video ended")
        break    
    out.write(frame)    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()