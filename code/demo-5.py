import streamlit as st
from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import pygame
import threading

# Initialize Dlib’s face detector
svm_predictor_path = 'SVMclassifier.dat'
EYE_AR_THRESH = 0.20
EYE_AR_CONSEC_FRAMES = 10
MOU_AR_THRESH = 1.2

# Alarm function
pygame.mixer.init()
def play_alarm():
    pygame.mixer.music.load("alarm.wav")    
    pygame.mixer.music.play()

# Functions for EAR and MAR
def EAR(drivereye):
    point1 = dist.euclidean(drivereye[1], drivereye[5])
    point2 = dist.euclidean(drivereye[2], drivereye[4])
    distance = dist.euclidean(drivereye[0], drivereye[3])
    return (point1 + point2) / (2.0 * distance)

def MOR(drivermouth):
    point = dist.euclidean(drivermouth[0], drivermouth[6])
    point1 = dist.euclidean(drivermouth[2], drivermouth[10])
    point2 = dist.euclidean(drivermouth[4], drivermouth[8])
    return (point1 + point2) / point

# Load SVM classifier and facial landmark predictor
svm_detector = dlib.get_frontal_face_detector()
svm_predictor = dlib.shape_predictor(svm_predictor_path)
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

# Streamlit Interface
st.title("Driver Drowsiness Monitoring System")
st.write("Real-time monitoring using Visual Behaviour and Machine Learning")

# Variables to control monitoring
monitoring = st.session_state.get("monitoring", False)
st.session_state.monitoring = False

if 'alarm_playing' not in st.session_state:
    st.session_state['alarm_playing'] = False
# Webcam Start and Stop Button
if st.button("Start Monitoring"):
    st.session_state.monitoring = True
if st.button("Stop Monitoring"):
    st.session_state.monitoring = False

# Monitoring loop
if st.session_state.monitoring:
    webcamera = cv2.VideoCapture(0)
    COUNTER = 0
    yawnStatus = False
    yawns = 0
    alarm_on = False

    # Create a place in Streamlit to display video frames
    frame_display = st.image([])

    while webcamera.isOpened() and st.session_state.monitoring:
        ret, frame = webcamera.read()
        if not ret:
            break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        prev_yawn_status = yawnStatus
        rects = svm_detector(gray, 0)

        for rect in rects:
            shape = svm_predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            mouth = shape[mStart:mEnd]

            leftEAR = EAR(leftEye)
            rightEAR = EAR(rightEye)
            mouEAR = MOR(mouth)
            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            mouthHull = cv2.convexHull(mouth)

            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 255), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 255), 1)
            cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)

            if ear < EYE_AR_THRESH:
                COUNTER += 1
                cv2.putText(frame, "Eyes Closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                if COUNTER >= EYE_AR_CONSEC_FRAMES and not alarm_on:
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    alarm_on = True
                    # a=st.audio('alarm.wav',autoplay=True)
                    threading.Thread(target=play_alarm).start()
            else:
                COUNTER = 0
                alarm_on = False
                cv2.putText(frame, "Eyes Open", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            cv2.putText(frame, "EAR: {:.2f}".format(ear), (480, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            if mouEAR > MOU_AR_THRESH:
                cv2.putText(frame, "Yawning, DROWSINESS ALERT!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                yawnStatus = True
                output_text = "Yawn Count: " + str(yawns + 1)
                cv2.putText(frame, output_text, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                if not alarm_on:
                    alarm_on = True
                    threading.Thread(target=play_alarm).start()
            else:
                yawnStatus = False
                alarm_on = False

            if prev_yawn_status and not yawnStatus:
                yawns += 1

            cv2.putText(frame, "MAR: {:.2f}".format(mouEAR), (480, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        frame_display.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(1) & 0xFF == ord("q") or not st.session_state.monitoring:
            webcamera.release()
            cv2.destroyAllWindows()
            break


else:
    st.write("Click 'Start Monitoring' to initiate drowsiness monitoring.")