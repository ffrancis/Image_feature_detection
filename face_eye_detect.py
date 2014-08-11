'''

Compiled by Felix Francis

Description:    Finds an object of predefined class in an image. Haar classifier implemented in opencv is used to identify and mark face and eye in images with reasonably large face and eyes.
                The code uses trained classifiers in two XML files. cv.Load() function loads the XML file into memory. cv.HaarDetectObjects() function detectes
                the objects

Input:          input_image.jpg image file
Returns:        Displays input_image.jpg with a rectangle (blue) over the detected face and a rectangle (red) over the detected eyes.
                A rectangle (red) is drawn over the detected eye if eye is in any detected face. A rectangle (blue) is drawn over the detected face if there is more than one eye detected in it.

Note: Use the provided "install_open_cv.sh" to install openCV in linux

For additional information, reffer: http://docs.opencv.org/trunk/doc/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html#py-table-of-content-feature2d


'''



import cv

inputimg = cv.LoadImage('input_image.jpg') # input image file for detecting face and eye
# classifiers are loaded
face_classifier = cv.Load('haarcascade_frontalface_default.xml')
eye_classfier = cv.Load('haarcascade_eye.xml')

# classifiers are run
mem_store = cv.CreateMemStorage()
face_detected = cv.HaarDetectObjects(inputimg, face_classifier, mem_store)
eye_detected = cv.HaarDetectObjects(inputimg, eye_classfier, mem_store)


num_eyes = 0

# a rectangle (red) is drawn over the detected eye if eye is in detected face
if face_detected:
    for face in face_detected:
        for eye in eye_detected:
            if eye[0][0] >= face[0][0] and eye[0][1] >= face[0][1] and (eye[0][0] + eye[0][2]) <= (face[0][0]+face[0][2]) and (eye[0][1] + eye[0][3]) <= (face[0][1]+face[0][3]):
                num_eyes += 1

                cv.Rectangle(inputimg,(eye[0][0],eye[0][1]),
                    (eye[0][0]+eye[0][2],eye[0][1]+eye[0][3]),
                    cv.RGB(255, 0, 0),2)
        


# a rectangle (blue) is drawn over the detected face if there are more than one eye detected in it
                if num_eyes > 0:
                    cv.Rectangle(inputimg,(face[0][0],face[0][1]),
                        (face[0][0]+face[0][2],face[0][1]+face[0][3]),
                        cv.RGB(0, 0, 255),2)        

cv.NamedWindow('Face Detection', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Face Detection', inputimg) 
cv.WaitKey()
