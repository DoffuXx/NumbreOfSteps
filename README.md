# Human Gait Analysis
This Python script analyzes human gait using computer vision and pose estimation. 
It uses the following libraries:

* cv2: OpenCV library for computer vision
* mediapipe: MediaPipe library for pose estimation
* math: Python math library
* numpy: NumPy library for numerical operations
* pandas: Pandas library for data analysis

## __Requirements__

* Python 3
* OpenCV
* mediapipe
* numpy
* pandas
## Installation
To install OpenCV:

```
pip install opencv-python
```
To install mediapipe:

```
pip install mediapipe
```
To install numpy:

```
pip install numpy
```
To install pandas:

```
pip install pandas
```
## How to use
1. Place the video file in the same directory as the script.
2. Open the script and replace "park.mp4" with the name of the video file you want to analyze.
3. Run the script.

The script will display the video with some additional information:

* Number of steps taken
* Speed of walking
* Distance traveled by each step
* Total distance traveled

The script uses computer vision and pose estimation to detect when a step is taken and to estimate the speed and distance traveled. The script uses the MediaPipe library to detect and track the position of the feet and legs, and calculates the distance traveled based on the position of the feet. The script then calculates the speed based on the distance traveled and the time taken for each step. Finally, the script displays the information on the screen.
