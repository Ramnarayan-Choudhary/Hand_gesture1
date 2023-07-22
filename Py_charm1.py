
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
