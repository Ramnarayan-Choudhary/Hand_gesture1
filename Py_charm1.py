# #
# # import numpy as np
# # import cv2
# #
# # # Hold the background frame for background subtraction.
# # background = None
# # # Hold the hand's data so all its details are in one place.
# # hand = None
# # # Variables to count how many frames have passed and to set the size of the window.
# # # fimport cv2
# #
# # frames_elapsed = 0
# # FRAME_HEIGHT = 200
# # FRAME_WIDTH = 300
# # CALIBRATION_TIME = 30
# # BG_WEIGHT = 0.5
# # OBJ_THRESHOLD = 18
# #
# # # Start the camera output
# # capture = cv2.VideoCapture(0)
# #
# # while True:
# #     # Store the frame from the video capture and resize it to the desired window size.
# #     ret, frame = capture.read()
# #     frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
# #
# #     cv2.imshow("Camera Input", frame)
# #     frames_elapsed += 1  # Increment the frames_elapsed variable
# #
# #     # Check if user wants to exit.
# #     if cv2.waitKey(1) & 0xFF == ord('x'):
# #         break
# #
# # # When we exit the loop, we have to stop the capture too.
# # # capture.release()
# # # cv2.destroyAllWindows()
# #
# #
# #
# # # Flip the frame over the vertical axis so that it works like a mirror, which is more intuitive to the user.
# # frame = cv2.flip(frame, 1)
# # # Our region of interest will be the top right part of the frame.
# # region_top = 0
# # region_bottom = int(2 * FRAME_HEIGHT / 3)
# # region_left = int(FRAME_WIDTH / 2)
# # region_right = FRAME_WIDTH
# #
# # frames_elapsed = 0
# #
# # frames_elapsed += 1
# #
# #
# # class HandData:
# #     top = (0,0)
# #     bottom = (0,0)
# #     left = (0,0)
# #     right = (0,0)
# #     centerX = 0
# #     prevCenterX = 0
# #     isInFrame = False
# #     isWaving = False
# #     fingers = 0
# #
# #     def __init__(self, top, bottom, left, right, centerX):
# #         self.top = top
# #         self.bottom = bottom
# #         self.left = left
# #         self.right = right
# #         self.centerX = centerX
# #         self.prevCenterX = 0
# #         isInFrame = False
# #         isWaving = False
# #
# #     def update(self, top, bottom, left, right):
# #         self.top = top
# #         self.bottom = bottom
# #         self.left = left
# #         self.right = right
# #
# #
# # # Here we take the current frame, the number of frames elapsed, and how many fingers we've detected
# # # so we can print on the screen which gesture is happening (or if the camera is calibrating).
# # def write_on_image(frame, hand):
# #     text = "Searching..."
# #
# #     if frames_elapsed < CALIBRATION_TIME:
# #         text = "Calibrating..."
# #     elif hand == None or hand.isInFrame == False:
# #         text = "No hand detected"
# #     else:
# #         if hand.isWaving:
# #             text = "Waving"
# #         elif hand.fingers == 0:
# #             text = "Rock"
# #         elif hand.fingers == 1:
# #             text = "Pointing"
# #         elif hand.fingers == 2:
# #             text = "Scissors"
# #
# #     cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.4,( 0 , 0 , 0 ),2,cv2.LINE_AA)
# #     cv2.putText(frame, text, (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255,255),1,cv2.LINE_AA)
# #
# # # Highlight the region of interest using a drawn rectangle.
# #     cv2.rectangle(display_frame, (region_left, region_top), (region_right, region_bottom), (255,255,255), 2)
# # # Write the action the hand is doing on the screen, and draw the region of interest.
# #     write_on_image(frame, hand)
# # def get_region(frame):
# #     # Separate the region of interest from the rest of the frame.
# #     region = frame[region_top:region_bottom, region_left:region_right]
# #     # Make it grayscale so we can detect the edges more easily.
# #     region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
# #     # Use a Gaussian blur to prevent frame noise from being labeled as an edge.
# #     region = cv2.GaussianBlur(region, (5,5), 0)
# #
# #     return region
# #     # Separate the region of interest and prep it for edge detection.
# #     region = get_region(frame)
# #
# #
# #
# # def get_average(region):
# #     # We have to use the global keyword because we want to edit the global variable.
# #     global background
# #     # If we haven't captured the background yet, make the current region the background.
# #     if background is None:
# #         background = region.copy().astype("float")
# #         return
# #     # Otherwise, add this captured frame to the average of the backgrounds.
# #     cv2.accumulateWeighted(region, background, BG_WEIGHT)
# #
# #
# #
# #
# #     if frames_elapsed < CALIBRATION_TIME:
# #         get_average(region)
# #
# # # Here we use differencing to separate the background from the object of interest.
# #
# #
# # def segment(region):
# #     global hand
# #
# #     # Find the absolute difference between the background and the current frame.
# #     diff = cv2.absdiff(background.astype(np.uint8), region)
# #
# #     # Threshold that region with a strict 0 or 1 ruling so only the foreground remains.
# #     thresholded_region = cv2.threshold(diff, OBJ_THRESHOLD, 255, cv2.THRESH_BINARY)[1]
# #
# #     # Get the contours of the region, which will return an outline of the hand.
# #     (_, contours, _) = cv2.findContours(thresholded_region.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# #
# #     # If we didn't get anything, there's no hand.
# #     if len(contours) == 0:
# #         if hand is not None:
# #             hand.isInFrame = False
# #         return
# #     # Otherwise return a tuple of the filled hand (thresholded_region), along with the outline (segmented_region).
# #     else:
# #         if hand is not None:
# #             hand.isInFrame = True
# #         segmented_region = max(contours, key=cv2.contourArea)
# #         return (thresholded_region, segmented_region)
# #
# #
# # if frames_elapsed < CALIBRATION_TIME:
# #     get_average(region)
# # else:
# #     region_pair = segment(region)
# #     if region_pair is not None:
# #         # If we have the regions segmented successfully, show them in another window for the user.
# #         (thresholded_region, segmented_region) = region_pair
# #
# #
# #
# # capture.release()
# # cv2.destroyAllWindows()
#
#
# import cv2
# import mediapipe as mp
# from tkinter import *
# import numpy as np
# import time
# def hold():
#     import pyautogui
#     # import HandTrackingModule as htm
#     cap = cv2.VideoCapture(0)
#     hand_detector = mp.solutions.hands.Hands()
#     drawing_utils = mp.solutions.drawing_utils
#     scree_width, screen_height = pyautogui.size()
#     pinky_y = 0
#     k_y = 0
#     pinky_x = 0
#     thumb_x = 0
#     index_x = 0
#
#     while True:
#         success, frame = cap.read()
#
#         frame = cv2.flip(frame, 1)
#         frame_height, frame_width, _ = frame.shape
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         output = hand_detector.process(rgb_frame)
#         hands = output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(frame, hand)
#                 landmarks = hand.landmark
#                 for id, landmark in enumerate(landmarks):
#                     x = int(landmark.x * frame_width)
#                     y = int(landmark.y * frame_height)
#                     print(x, y)
#                     if id == 4:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         thumb_x = scree_width / frame_width * x
#                         thumb_y = screen_height / frame_height * y
#                     if id == 13:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         pinky_x = scree_width / frame_width * x
#                         pinky_y = screen_height / frame_height * y
#
#                     if id == 8:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         k_x = scree_width / frame_width * x
#                         k_y = screen_height / frame_height * y
#                         pyautogui.moveTo(k_x, k_y)
#
#                     if id == 5:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         index_x = scree_width / frame_width * x
#                         index_y = screen_height / frame_height * y
#
#                         # if abs(pinky_y - k_y)<60:
#                         #     pyautogui.click()
#                         #     pyautogui.sleep(1)
#                         if abs(pinky_x - thumb_x) < 20:
#                             pyautogui.mouseUp()
#                             pyautogui.FAILSAFE = False
#                         # if abs(thumb_x - index_x) < 60:
#                         #     pyautogui.hotkey('Alt','F4')
#                         #     pyautogui.sleep(1)
#                         if abs(thumb_x - index_x) < 20:
#                             pyautogui.mouseDown()
#
#                         #     pyautogui.dragTo(pinky_x+100, pinky_y+200,2, button='left')
#
#                         # if abs(pinky_x - thumb_x) < 80:
#                         #     if abs(pinky_y - k_y) < 80:
#                         #         # pyautogui.write('welcome sir , welcome mam', interval=1)
#                         #         pyautogui.press('volumeup')
#                         #         pyautogui.sleep(1)
#
#         cv2.imshow("mouse", frame)
#         cv2.waitKey(1)
# def vol2():
#     # import cv2
#     # import mediapipe as mp
#     # from tkinter import *
#     # import numpy as np
#     import pyautogui
#
#     cap = cv2.VideoCapture(0)
#     hand_detector = mp.solutions.hands.Hands()
#     drawing_utils = mp.solutions.drawing_utils
#     scree_width, screen_height = pyautogui.size()
#     pinky_y = 0
#     hey_x = 0
#     pinky_x = 0
#     thumb_x = 0
#     thumb_y = 0
#     index_x = 0
#     my_y = 0
#     my_x = 0
#     new_x = 0
#     index_y = 0
#     from ctypes import cast, POINTER
#     from comtypes import CLSCTX_ALL
#     from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#
#     devices = AudioUtilities.GetSpeakers()
#     interface = devices.Activate(
#         IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#     volume = cast(interface, POINTER(IAudioEndpointVolume))
#     # volume.GetMute()
#     # volume.GetMasterVolumeLevel()
#     volRange = volume.GetVolumeRange()
#     volume.SetMasterVolumeLevel(-10, None)
#     minVol = volRange[0]
#     maxVol = volRange[1]
#     while True:
#         success, frame = cap.read()
#
#         frame = cv2.flip(frame, 1)
#         frame_height, frame_width, _ = frame.shape
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         output = hand_detector.process(rgb_frame)
#         hands = output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(frame, hand)
#                 landmarks = hand.landmark
#                 for id, landmark in enumerate(landmarks):
#                     x = int(landmark.x * frame_width)
#                     y = int(landmark.y * frame_height)
#                     print(x, y)
#                     if id == 4:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         thumb_x = scree_width / frame_width * x
#                         thumb_y = screen_height / frame_height * y
#                     if id == 1:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         pinky_x = scree_width / frame_width * x
#                         pinky_y = screen_height / frame_height * y
#
#                     if id == 12:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         my_x = scree_width / frame_width * x
#                         my_y = screen_height / frame_height * y
#
#                     if id == 13:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         hey_x = scree_width / frame_width * x
#                         hey_y = screen_height / frame_height * y
#                     if id == 8:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         new_x = scree_width / frame_width * x
#                         new_y = screen_height / frame_height * y
#                         pyautogui.moveTo(new_x, new_y)
#
#                     # if abs(hey_x - thumb_x) < 20:
#                     #     pyautogui.press('volumedown')
#                     #     pyautogui.sleep(0.1)
#                     #     pyautogui.FAILSAFE = False
#                     if id == 5:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         index_x = scree_width / frame_width * x
#                         index_y = screen_height / frame_height * y
#
#                     if abs(my_y - pinky_y) < 50:
#                         length = abs(index_x - thumb_x)
#                         print(length)
#                         vol = np.interp(length, [50, 300], [minVol, maxVol])
#                         volume.SetMasterVolumeLevel(vol, None)
#                     else:
#                         if abs(thumb_x - index_x) < 20:
#                             pyautogui.click()
#                             pyautogui.sleep(0.1)
#                         if abs(hey_x - thumb_x) < 40:
#                             pyautogui.doubleClick()
#                             pyautogui.sleep(0.1)
#                             # pyautogui.FAILSAFE = False
#
#         cv2.imshow("mouse", frame)
#         cv2.waitKey(1)
# def vol():
#     import pyautogui
#     cap = cv2.VideoCapture(0)
#     hand_detector = mp.solutions.hands.Hands()
#     drawing_utils = mp.solutions.drawing_utils
#     scree_width, screen_height = pyautogui.size()
#     pinky_y = 0
#     hey_x = 0
#     pinky_x = 0
#     thumb_x = 0
#     index_x = 0
#
#     while True:
#         success, frame = cap.read()
#
#         frame = cv2.flip(frame, 1)
#         frame_height, frame_width, _ = frame.shape
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         output = hand_detector.process(rgb_frame)
#         hands = output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(frame, hand)
#                 landmarks = hand.landmark
#                 for id, landmark in enumerate(landmarks):
#                     x = int(landmark.x * frame_width)
#                     y = int(landmark.y * frame_height)
#                     print(x, y)
#                     if id == 4:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         thumb_x = scree_width / frame_width * x
#                         thumb_y = screen_height / frame_height * y
#                     if id == 9:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         pinky_x = scree_width / frame_width * x
#                         pinky_y = screen_height / frame_height * y
#                         pyautogui.moveTo(pinky_x, pinky_y)
#
#
#                     if id == 13:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         hey_x = scree_width / frame_width * x
#                         hey_y = screen_height / frame_height * y
#
#
#                     if abs(hey_x - thumb_x) < 20:
#                         pyautogui.press('volumedown')
#                         pyautogui.sleep(0.1)
#                         pyautogui.FAILSAFE = False
#                     if id == 5:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         index_x = scree_width / frame_width * x
#                         index_y = screen_height / frame_height * y
#
#                         # if abs(pinky_y - k_y)<60:
#                         #     pyautogui.click()
#                         #     pyautogui.sleep(1)
#                         # if abs(pinky_x - thumb_x) < 40:
#                         #     pyautogui.doubleClick()
#                         #     pyautogui.sleep(1)
#                         #     pyautogui.FAILSAFE= False
#                         # if abs(thumb_x - index_x) < 60:
#                         #     pyautogui.hotkey('Alt','F4')
#                         #     pyautogui.sleep(1)
#                         if abs(thumb_x - index_x) < 20:
#                             # if abs(pinky_x - thumb_x) < 80:
#                             #     if abs(pinky_y - k_y) < 80:
#                             #         # pyautogui.write('welcome sir , welcome mam', interval=1)
#                                     pyautogui.press('volumeup')
#                                     pyautogui.sleep(1)
#
#         cv2.imshow("mouse", frame)
#         cv2.waitKey(1)
# def scroll():
#     import pyautogui
#     cap = cv2.VideoCapture(0)
#     hand_detector = mp.solutions.hands.Hands()
#     drawing_utils = mp.solutions.drawing_utils
#     screen_width, screen_height = pyautogui.size()
#     thumb_x = 0
#     hey_x = 0
#     index_y = 0
#     index_x = 0
#     pinky_x=0
#     pinky_y = 0
#
#     while True:
#         _, frame = cap.read()
#         frame = cv2.flip(frame, 1)
#         frame_height, frame_width, _ = frame.shape
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         output = hand_detector.process(rgb_frame)
#         hands = output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(frame, hand)
#                 landmarks = hand.landmark
#                 for id, landmark in enumerate(landmarks):
#                     x = int(landmark.x * frame_width)
#                     y = int(landmark.y * frame_height)
#                     if id == 8:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         index_x = (screen_width + 200) / frame_width * x
#                         index_y = (screen_height + 200) / frame_height * y
#                         # print(index_x,index_y)
#                         if index_x <= 1920:
#                             if index_y <= 1083:
#                                 pyautogui.moveTo(index_x, index_y)
#
#                     if id == 4:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         thumb_x = screen_width / frame_width * x
#                         thumb_y = screen_height / frame_height * y
#                         # print('outside', abs(index_y - thumb_y))
#                         if abs(index_y - thumb_y) < 10:
#                             pyautogui.click()
#                             pyautogui.sleep(0.1)
#                     if id == 5:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         pinky_x = screen_width / frame_width * x
#                         pinky_y = screen_height / frame_height * y
#                         if abs(pinky_x - thumb_x) < 20:
#                             pyautogui.scroll(-40)
#                             pyautogui.sleep(0.1)
#                             pyautogui.FAILSAFE = False
#
#                     if id == 13:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         hey_x = screen_width / frame_width * x
#                         hey_y = screen_height / frame_height * y
#
#                         if abs(hey_x - thumb_x) < 10:
#                             pyautogui.scroll(40)
#                             pyautogui.sleep(0.1)
#                             pyautogui.FAILSAFE = False
#                     # if abs(thumb_x - index_x) < 20:
#                     #     if abs(pinky_x - thumb_x) < 80:
#                     #         if abs(pinky_y - hey_y) < 80:
#                     #             # pyautogui.write('welcome sir , welcome mam', interval=1)
#                     #             pyautogui.press('volumeup')
#                     #             pyautogui.sleep(1)
#         cv2.imshow('Virtual Mouse', frame)
#         cv2.waitKey(1)
# def click():
#     import pyautogui
#     cap = cv2.VideoCapture(0)
#     hand_detector = mp.solutions.hands.Hands()
#     drawing_utils = mp.solutions.drawing_utils
#     screen_width, screen_height = pyautogui.size()
#     thumb_x = 0
#     hey_x = 0
#     index_y = 0
#
#     while True:
#         _, frame = cap.read()
#         frame = cv2.flip(frame, 1)
#         frame_height, frame_width, _ = frame.shape
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         output = hand_detector.process(rgb_frame)
#         hands = output.multi_hand_landmarks
#         if hands:
#             for hand in hands:
#                 drawing_utils.draw_landmarks(frame, hand)
#                 landmarks = hand.landmark
#                 for id, landmark in enumerate(landmarks):
#                     x = int(landmark.x * frame_width)
#                     y = int(landmark.y * frame_height)
#                     if id == 8:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         index_x = (screen_width + 200) / frame_width * x
#                         index_y = (screen_height + 200) / frame_height * y
#                         # print(index_x,index_y)
#                         if index_x <= 1920:
#                             if index_y <= 1083:
#                                 pyautogui.moveTo(index_x, index_y)
#
#                     if id == 4:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         thumb_x = screen_width / frame_width * x
#                         thumb_y = screen_height / frame_height * y
#                         # print('outside', abs(index_y - thumb_y))
#                         if abs(index_y - thumb_y) < 10:
#                             pyautogui.click()
#                             pyautogui.sleep(0.1)
#                     if id == 5:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         pinky_x = screen_width / frame_width * x
#                         pinky_y = screen_height / frame_height * y
#                         if abs(pinky_x - thumb_x) < 20:
#                             pyautogui.click()
#                             pyautogui.sleep(0.5)
#                             pyautogui.FAILSAFE = False
#
#                     if id == 13:
#                         cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
#                         hey_x = screen_width / frame_width * x
#                         hey_y = screen_height / frame_height * y
#
#
#                         if abs(hey_x - thumb_x) < 10:
#                             pyautogui.doubleClick()
#                             pyautogui.sleep(0.1)
#                             pyautogui.FAILSAFE = False
#         #
#         cv2.imshow('Virtual Mouse', frame)
#         cv2.waitKey(1)
#
#
# cap.release()
# cv2.destroyAllWindows()
#
# # abhi = Tk()
# # abhi.geometry("200x100")
# # abhi.title("Controls")
# #
# # mymenu= Menu(abhi)
# # m1 = Menu(mymenu, tearoff=0)
# # m1.add_command(label="double and single click mode", command=click)
# # m1.add_command(label="volume up/down mode", command=vol)
# # mymenu.add_cascade(label="Click/Volume",menu=m1)
# #
# #
# # m2 = Menu(mymenu,tearoff=0)
# # m2.add_command(label="scroll up/down", command=scroll)
# # m2.add_command(label="vol+double click", command=vol2)
# # m2.add_command(label="hold", command=hold)
# # abhi.configure(menu=mymenu)
# # mymenu.add_cascade(label="scroll/hold" , menu=m2)
# #
# # mymenu.add_command(label="Parityaj", command=quit)
# # # m2.add_command(label="zoom In/out", command=zoom)
# # # m2.add_command(label="")
# #
# #
# #
# # abhi.mainloop()
#
#
import cv2
import mediapipe as mp
import pyautogui

def hold():
    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    pinky_y = 0
    k_y = 0
    pinky_x = 0
    thumb_x = 0
    index_x = 0

    while True:
        success, frame = cap.read()

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                    if id == 13:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        pinky_x = screen_width / frame_width * x
                        pinky_y = screen_height / frame_height * y
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        k_x = screen_width / frame_width * x
                        k_y = screen_height / frame_height * y
                        pyautogui.moveTo(k_x, k_y)
                    if id == 5:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y
                        if abs(pinky_y - k_y) < 60:
                            pyautogui.click()
                            pyautogui.sleep(1)
                        if abs(pinky_x - thumb_x) < 20:
                            pyautogui.mouseUp()
                            pyautogui.FAILSAFE = False
                        if abs(thumb_x - index_x) < 60:
                            pyautogui.hotkey('Alt', 'F4')
                            pyautogui.sleep(1)
                        if abs(thumb_x - index_x) < 60:
                            pyautogui.mouseDown()

        cv2.imshow("mouse", frame)
        cv2.waitKey(1)


def vol2():
    import pyautogui

    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    pinky_y = 0
    hey_x = 0
    pinky_x = 0
    thumb_x = 0
    thumb_y = 0
    index_x = 0
    my_y = 0
    my_x = 0
    new_x = 0
    index_y = 0
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volRange = volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-10, None)
    minVol = volRange[0]
    maxVol = volRange[1]

    while True:
        success, frame = cap.read()

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                    if id == 1:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        pinky_x = screen_width / frame_width * x
                        pinky_y = screen_height / frame_height * y
                    if id == 12:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        my_x = screen_width / frame_width * x
                        my_y = screen_height / frame_height * y
                    if id == 13:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        hey_x = screen_width / frame_width * x
                        hey_y = screen_height / frame_height * y
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        new_x = screen_width / frame_width * x
                        new_y = screen_height / frame_height * y
                        pyautogui.moveTo(new_x, new_y)
                    if abs(hey_x - thumb_x) < 20:
                        pyautogui.press('volumedown')
                        pyautogui.sleep(0.1)
                        pyautogui.FAILSAFE = False
                    if id == 5:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y
                        if abs(my_y - pinky_y) < 50:
                            length = abs(index_x - thumb_x)
                            vol = np.interp(length, [50, 300], [minVol, maxVol])
                            volume.SetMasterVolumeLevel(vol, None)
                        else:
                            if abs(thumb_x - index_x) < 20:
                                pyautogui.click()
                                pyautogui.sleep(0.1)
                            if abs(hey_x - thumb_x) < 40:
                                pyautogui.doubleClick()
                                pyautogui.sleep(0.1)

        cv2.imshow("mouse", frame)
        cv2.waitKey(1)


def vol():
    import pyautogui

    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    pinky_y = 0
    hey_x = 0
    pinky_x = 0
    thumb_x = 0
    index_x = 0

    while True:
        success, frame = cap.read()

        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                    if id == 9:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        pinky_x = screen_width / frame_width * x
                        pinky_y = screen_height / frame_height * y
                        pyautogui.moveTo(pinky_x, pinky_y)
                    if id == 13:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        hey_x = screen_width / frame_width * x
                        hey_y = screen_height / frame_height * y
                    if abs(hey_x - thumb_x) < 20:
                        pyautogui.press('volumedown')
                        pyautogui.sleep(0.1)
                        pyautogui.FAILSAFE = False
                    if id == 5:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = screen_width / frame_width * x
                        index_y = screen_height / frame_height * y
                        if abs(pinky_y - k_y) < 60:
                            pyautogui.click()
                            pyautogui.sleep(1)
                        if abs(pinky_x - thumb_x) < 40:
                            pyautogui.doubleClick()
                            pyautogui.sleep(1)
                            pyautogui.FAILSAFE = False
                        if abs(thumb_x - index_x) < 60:
                            pyautogui.hotkey('Alt', 'F4')
                            pyautogui.sleep(1)
                        if abs(thumb_x - index_x) < 60:
                            pyautogui.press('volumeup')
                            pyautogui.sleep(1)

        cv2.imshow("mouse", frame)
        cv2.waitKey(1)


def scroll():
    import pyautogui

    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    thumb_x = 0
    hey_x = 0
    index_y = 0
    index_x = 0
    pinky_x = 0
    pinky_y = 0

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = (screen_width + 200) / frame_width * x
                        index_y = (screen_height + 200) / frame_height * y
                        if index_x <= 1920:
                            if index_y <= 1083:
                                pyautogui.moveTo(index_x, index_y)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                        if abs(index_y - thumb_y) < 10:
                            pyautogui.click()
                            pyautogui.sleep(0.1)
                    if id == 5:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        pinky_x = screen_width / frame_width * x
                        pinky_y = screen_height / frame_height * y
                        if abs(pinky_x - thumb_x) < 20:
                            pyautogui.scroll(-40)
                            pyautogui.sleep(0.1)
                            pyautogui.FAILSAFE = False
                    if id == 13:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        hey_x = screen_width / frame_width * x
                        hey_y = screen_height / frame_height * y
                        if abs(hey_x - thumb_x) < 10:
                            pyautogui.scroll(40)
                            pyautogui.sleep(0.1)
                            pyautogui.FAILSAFE = False

        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)


def click():
    import pyautogui

    cap = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    thumb_x = 0
    hey_x = 0
    index_y = 0

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = (screen_width + 200) / frame_width * x
                        index_y = (screen_height + 200) / frame_height * y
                        if index_x <= 1920:
                            if index_y <= 1083:
                                pyautogui.moveTo(index_x, index_y)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width / frame_width * x
                        thumb_y = screen_height / frame_height * y
                        if abs(index_y - thumb_y) < 10:
                            pyautogui.click()
                            pyautogui.sleep(0.1)
                    if id == 5:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        pinky_x = screen_width / frame_width * x
                        pinky_y = screen_height / frame_height * y
                        if abs(pinky_x - thumb_x) < 20:
                            pyautogui.click()
                            pyautogui.sleep(0.5)
                            pyautogui.FAILSAFE = False
                    if id == 13:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        hey_x = screen_width / frame_width * x
                        hey_y = screen_height / frame_height * y
                        if abs(hey_x - thumb_x) < 10:
                            pyautogui.doubleClick()
                            pyautogui.sleep(0.1)
                            pyautogui.FAILSAFE = False

        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)


# cap.release()
cv2.destroyAllWindows()
