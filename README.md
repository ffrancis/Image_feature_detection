Face and eye detection from images using openCV:
================================================

A Python code that detects and marks face and eye from images with reasonably large face/faces [and so eyes ;)] using openCV


Input image:
================================================
![alt tag](https://github.com/ffrancis/Image_feature_detection/blob/master/input_image.jpg)

Output image:
================================================
![alt tag](https://github.com/ffrancis/Image_feature_detection/blob/master/output_image.jpg)

Dependencies:
=============

You will need to install openCV first:
	Use the provided "install_open_cv.sh" to install openCV in linux
	Warning: installation on openCV takes considerable time


Compiled by Felix Francis

Description:    Finds an object of predifined class in an image. Haar classifier implemented in opencv is used to identify and mark face and eye in images with reasonably large face and eyes.
                The code uses trained classifiers in two XML files. cv.Load() function loads the XML file into memory. cv.HaarDetectObjects() function detectes
                the objects

Input:          Input_image.jpg image file
Returns:        Displays input_image.jpg with a rectangle (blue) over the detected face and a rectangle (red) over the detected eyes.
                A rectangle (red) is drawn over the detected eye if eye is in any detected face. A rectangle (blue) is drawn over the detected face if there is more than one eye detected in it.

Note: Use the provided "install_open_cv.sh" to install openCV in linux

For additional information: http://docs.opencv.org/trunk/doc/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html#py-table-of-content-feature2d


Additional functions:
=====================
You can use other haar classifiers to detect other specific features in images.
