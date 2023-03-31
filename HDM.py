#importing the necessary libraries
import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands=mp.solutions.hands

mp_hands = mp.solutions.hands #calling the hands class 


#utilising openCV for video caputuring for display live usage
cap = cv2.VideoCapture(0) #find the right webcam, in this case mine is zero
hands = mphands.Hands() #initiating the hands variable
while True:
    data, image = cap.read() #opencv reads these two variables
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #processing image

    #storing the results within this variable for hands + patterns
    results=hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if results.multi_hand_landmarks:    #drawing the landmarks for the hands 
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
            image,                  
            hand_landmarks,
            mphands.HAND_CONNECTIONS)
            cv2.imshow('Handtracker', image) #title of the project "handtracker"
            cv2.waitKey(1)
             
         



            