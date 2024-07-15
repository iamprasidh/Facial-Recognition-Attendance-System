import csv
import os
import cv2

# Function to capture user images and update CSV file
def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech):
    if l1 == "" or l2 == "":
        t = 'Please enter your Enrollment Number and Name.'
        text_to_speech(t)
        return
    
    Enrollment = l1
    Name = l2
    
    try:
        # Initialize camera and face detector
        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier(haarcasecade_path)
        
        # Create directory for saving images
        directory = f"{Enrollment}_{Name}"
        path = os.path.join(trainimage_path, directory)
        os.makedirs(path, exist_ok=True)
        
        sampleNum = 0
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                sampleNum += 1
                # Save image with unique name
                img_name = f"{Name}_{Enrollment}_{sampleNum}.jpg"
                cv2.imwrite(os.path.join(path, img_name), gray[y:y+h, x:x+w])
                cv2.imshow("Frame", img)
            
            if cv2.waitKey(1) & 0xFF == ord("q") or sampleNum > 50:
                break
        
        cam.release()
        cv2.destroyAllWindows()
        
        # Update CSV file with enrollment number and name
        with open("C:\\Users\\prasi\\Desktop\\FRAS\\StudentDetails\\studentdetails.csv", "a+", newline="") as csvFile:
            writer = csv.writer(csvFile, delimiter=",")
            writer.writerow([Enrollment, Name])
        
        # Display success message
        res = f"Images saved for Enrollment No: {Enrollment}, Name: {Name}"
        message.configure(text=res)
        text_to_speech(res)
    
    except Exception as e:
        err_screen.configure(text=str(e))
        text_to_speech(str(e))

