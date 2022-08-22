import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
thumb1_y=0
while True:
    _, frame = cam.read()
    frame=cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
                if id ==8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb1_x = screen_width / frame_width * x
                    thumb1_y = screen_height / frame_height * y
                    pyautogui.moveTo(thumb1_x,thumb1_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb2_x = screen_width / frame_width * x
                    thumb2_y = screen_height / frame_height * y
                    print('outside', abs(thumb1_y - thumb2_y))
                    if abs(thumb1_y - thumb2_y) < 25:
                        pyautogui.click()
                        pyautogui.sleep(1)



    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
