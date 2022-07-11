# HAND-GESTURE-RECOGNITION :star_struck: :+1: :point_up_2: :v: :metal: :point_down:

[![Generic badge](https://img.shields.io/badge/advance-Python3-yellowgreen)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/module-numpy-ff69b4)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/module%20-cv2-success)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/computer-vision-blueviolet)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/module-math-critical)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/python-3.6-green)](https://shields.io/) 
<br>

***This new Hand Gesture Recognition Software using Python3 is created by Biswarup Bhattacharjee, student of BTECH, in University of Engineering and Management, Kolkata.***

**Email Id: bbiswa471@gmail.com.** 

**Contact No: 916290272740.** 


<p align="left">
<a href="https://www.facebook.com/profile.php?id=100070395300810" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="biswa2210" height="30" width="40" /></a>
<a href="https://instagram.com/biswarup2210" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="" height="30" width="40" /></a>
<a href="https://github.com/biswa2210/biswa2210" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="" height="30" width="40" /></a>
</p>

## About :point_down: 

</div align="justified">

**This is a software or program which counts user's number of fingers shown before the webcam. When user takes his hand before the camera and shows fingures we can see the number is shown.** We can show fingures in many ways, which ever we want. It shows appropiate and correct result. In a day-to-day life, hand gesture recognition is one of the system that can detect the gesture of hand in a real time video. The gesture of hand is classify within a certain area of interest. Designing a system for hand gesture recognition is one of the goal of achieving the objectives of this project. The task of recognizing hand gestures is one of the main and important issues in computer vision. With the latest advances in information and media technology, human computer interaction (HCI) systems that involve hand processing tasks such as hand detection and hand gesture recognition. In this study, designing of the hand gesture recognition is one of the complicated job that involves two major problem. Firstly is the detection of hand. User hand is detected by using webcam in real-time video. The problem would be the unstable brightness, noise, poor resolution and contrast. The detected hand in the video are recognized to identify the gestures. At this stage, the process involves are the segmentation and edge detection. This study comprises on how to implement a complete system that can detect, recognizing and interpreting the hand by using Python and OpenCV in any intensity of light, pose or orientation of hand. In order to accomplish this, a real-time gesture based system is developed. In the proposal stage, designing a system that could detect the hand through the contour of the hand. The contour of the hand refers to the curve for a two variables for the function along which that function has a contact value that is not changed. Besides, to detect the appearance of hand in a frame of the real-time video, I will be using the Haar-cascade Classifier to track the appearance of hand before the image-processing is done. The result of the appearance of hand that the system could detect will be validated for analysis. For hardware implementation section, a wired web camera is used thus the hand gesture recognition can be done and implemented. 
</div>

## The Software uses :point_down:
 - [x] open Computer vision through web camera

**:point_right: [click here to view or download Demo Video of this project](https://drive.google.com/file/d/17t7bh1p3gi6wsdNxaq9kjEimxq_6J99D/view)**

## Purpose :point_down:

</div align="justified">

The goal of static hand gesture recognition is to classify the given hand gesture data represented by some features into some predefined finite number of gesture classes. The main objective of this effort is to explore the utility of two feature extraction methods, namely, hand contour and complex moments to solve the hand gesture recognition problem by identifying the primary advantages and disadvantages of each method.
</div>

## Use :point_down:

User just has to take his hand before the web cam and run the program. Then he can see the number of fingures shown. :raised_hand: :v:

## Conclusion and Future Works :point_down:

</div align="justified">

A new method for hand gesture recognition is introduced in this paper. The hand region is detected from the background by the background subtraction method. Then, the palm and fingers are segmented. On the basis of the segmentation, the fingers in the hand image are discovered and recognized. The recognition of hand gestures is accomplished by a simple rule classifier. The performance of our method is evaluated on a data set of 1300 hand images. The experimental results show that our approach performs well and is fit for the real-time applications. Moreover, the proposed method outperforms the state-of-art FEMD on an image collection of hand gestures. The performance of the proposed method highly depends on the result of hand detection. If there are moving objects with the color similar to that of the skin, the objects exist in the result of the hand detection and then degrade the performance of the hand gesture recognition. However, the machine learning algorithms can discriminate the hand from the background. ToF cameras provide the depth information that can improve the performance of hand detection. So, in future works, machine learning methods and ToF cameras may be used to address the complex background problem and improve the robustness of hand detection.
</div>

## Folder Structure :point_down:

```bash
HAND-GESTURE-RECOGNITION
     ├── .idea
     |      ├── inspectionProfiles
     |      |          └── profiles_settings.xml
     |      ├── HAND GESTURE RECOGNITION.iml
     |      ├── misc.xml
     |      └── modules.xml
     ├── capture.png
     ├── hand gesture recognition.py
     └── part1.py

```                       
## Making :point_down:

</div align="justified">

I have made this hand gesture recognition using python3. First, the hand is detected using the background subtraction method and the result of hand detection is transformed to a binary image. Then, the fingers and palm are segmented so as to facilitate the finger recognition. Moreover, the fingers are detected and recognized. Last, hand gestures are recognized using a simple rule classifier. I have installed opencv module for live detection using web camera .I have done this for capturing and reading the images.I have taken in rectangle.I have used gausian blur. I have converted the rgb(red green blue) images in hsv(hue saturation value). I have used dialusion andd erosion for filtering the images. I have used threshold function. I have used contours grid for counting the fingers in hand.
</div>

## Screenshots :point_down: 

<div align="center">
<a href="pics/hg1.PNG"><img src="pics/hg1.PNG" width="400" height= "250"></a> <a href="pics/hg2.PNG"><img src="pics/hg2.PNG" width="400" height= "250"></a>

<a href="pics/hg3.PNG"><img src="pics/hg3.PNG" width="400" height= "250"></a> <a href="pics/hg4.PNG"><img src="pics/hg4.PNG" width="400" height= "250"></a>

<a href="pics/hg5.PNG"><img src="pics/hg5.PNG" width="400" height= "250"></a> <a href="pics/hg6.PNG"><img src="pics/hg6.PNG" width="400" height= "250"></a>

<a href="pics/hg7.PNG"><img src="pics/hg7.PNG" width="400" height= "250"></a> <a href="pics/hg8.PNG"><img src="pics/hg8.PNG" width="400" height= "250"></a>
</div>


