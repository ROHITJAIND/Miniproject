# REAL TIME DRIVER FATIGUE ALERT SYSTEM
Driver fatigue and drowsiness are major causes of road accidents, necessitating an automated, real-time drowsiness detection system that accurately monitors drivers and alerts them to early signs of fatigue, as traditional methods often prove ineffective.
## About
Drowsiness while driving is a major cause of road accidents, especially among drivers who operate vehicles for extended periods, such as truck and bus drivers. ​
This issue results in thousands of injuries and crashes worldwide each year, with severe consequences. ​
Developing technologies to detect and prevent driver drowsiness is a critical challenge in accident prevention systems. ​
The objective of this project is to create a simulation that models a drowsiness detection system, which provides alerts specifically when the driver’s eyes are closed, aiming to reduce such accidents effectively. 

## Features
- **Eye Aspect Ratio (EAR) Calculation**: Measures eye openness to detect prolonged eye closure, indicating potential drowsiness.
- **Mouth Aspect Ratio (MAR) Calculation**: Detects yawning by measuring mouth openness as a sign of drowsiness.
- **Real-Time Face Detection**: Uses Dlib to detect faces and landmarks in live video frames.
- **Facial Landmark Detection**: Identifies key points around eyes and mouth to calculate EAR and MAR.
- **Drowsiness Alert System**: Triggers an audio alarm if drowsiness is detected based on EAR or MAR thresholds.
- **GUI with Streamlit**: Provides a user-friendly interface with Start/Stop buttons and real-time feedback on drowsiness.
- **Video Overlay with OpenCV**: Displays live video with annotated EAR/MAR values, alerts, and eye/mouth status.
- **Multithreading for Alarm**: Plays alarm sound on a separate thread to avoid interrupting video processing.


## Requirements
- **Hardware**:
  - Webcam (1080p recommended)
  - CPU: Intel i5 or better
  - RAM: 4 GB (8 GB recommended)
  - Speakers (for alarm)
  - Optional: NVIDIA GPU
- **Software**:
  - OS: Windows, macOS, or Linux
  - Python 3.7+
- **Python Libraries**:
  - Streamlit: `pip install streamlit`
  - OpenCV: `pip install opencv-python`
  - Dlib: `pip install dlib`
  - Imutils: `pip install imutils`
  - SciPy: `pip install scipy`
  - Pygame: `pip install pygame`
- **Optional**:
  - CMake (for Dlib installation): `sudo apt-get install cmake`
  - CUDA (for GPU acceleration, if needed)


## System Architecture
![alt text](<img/OUTPUT (1).png>)


## Output

<!--Embed the Output picture at respective places as shown below as shown below-->
#### Output1 - Home page
![alt text](<img/OUTPUT (2).png>)

#### Output2 - Eyes and Mouth Detected
![alt text](<img/OUTPUT (3).png>)

#### Output3 - Eyes Close Detected
![alt text](<img/OUTPUT (4).png>)

#### Output4 - Yawning Detected
![alt text](<img/OUTPUT (5).png>)

## Results and Impact
### Key Features

- **Facial Landmark Detection**: Dlib accurately detects facial points, ensuring precise eye and mouth tracking.
- **EAR & MAR Calculations**: Euclidean distance helps accurately detect closed eyes and yawning. EAR drop and high MAR correlate with drowsiness events.
- **Convex Hull Visualization**: OpenCV highlights eye and mouth regions effectively in real-time.
- **Real-Time Alarm System**: Pygame triggers alarms promptly upon detecting drowsiness.
## Articles published / References

- [1] Muhammad Ramzan et al., "A survey on state-of-the-art drowsiness detectiontechniques", IEEE Access, vol. 7, pp. 61904-61919, 2019.<br>
- [2] Swati Srivastava, "On the physiological measures based driver’s drowsinessdetection", 2021 5th International Conference on Information Systems and Computer Networks(ISCON), 2021.<br>
- [3] R. B. Salikhov, V. Kh Abdrakhmanov and I. N. Safargalin, "Internet of things (IoT)security alarms on ESP32-CAM", Journal of Physics: Conference Series, vol. 2096, no. 1, 2021.<br>
- [4] Vedat Ozan Oner, Developing IoT Projects With ESP32: Automate Your Home orBusiness With Inexpensive Wi-Fi Devices, Packt Publishing Ltd, 2021.<br>
- [5] B. N. Manu, "Facial features monitoring for real time drowsiness detection", In 201612th International Conference on Innovations in information technology (IIT), pp. 1-4, 2016, November.<br>
- [6] N. Irtija, M. Sami and M. A. R. Ahad, "Fatigue detection using facial landmarks", InInternational Symposium on Affective Science and Engineering ISASE2018, pp. 1-6, 2018.<br>
- [7] Vahid Kazemi and Josephine Sullivan, "One millisecond face alignment with anensemble of regression trees", Proceedings of the IEEE conference on computer vision andpattern recognition, 2014.<br>
- [8] R. B. Salikhov, V. Kh Abdrakhmanov and I. N. Safargalin, "Internet of things (IoT)security alarms on ESP32-CAM", Journal of Physics: Conference Series, vol. 2096, no. 1, 2021.




