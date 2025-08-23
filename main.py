import cv2

def main():
    cam=cv2.VideoCapture(0)

    if not cam.isOpened():
        raise RuntimeError("failed to open the cam try index 1 or 2")
    
    #we will create a window for the cam
    
    cv2.namedWindow("angelNo111",cv2.WINDOW_NORMAL)

    #NOW WE WANT TO OUR CAMERA TO CAPTURE THE VIDEO AND NOT JUST OPEN IT SO WE WILL CREATE A WHILE LOOP AND MAKE SURE IF SOME INTERUPTION HAPPENS THEN THE CAMERA SHUTS OFF
    while True:
        ret,frame=cam.read()

        #ret is a boolean value u can call it return to know if the frame was captured or not (frame is the single image odf the video)or some issue occured like camera unplugged
        #frame is the single image captured by the camera, we want it in video form thats why the while loop

        if not ret:
            print("failed to grab frame")
            #if you dont write break your camera will keep runing even if you click close button
            break
        
        #adjusting frame 
        frame=cv2.flip(frame,1)
        #displaig each image/frame captured in the window we created earlier
        cv2.imshow("angelNo111",frame)

        if cv2.getWindowProperty("angelNo111", cv2.WND_PROP_VISIBLE) < 1:
            break
        key = cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()


