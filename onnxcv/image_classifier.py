import cv2 
import numpy as np
import onnxruntime as rt
from skimage.transform import resize

'''

This is the ImageClassifier class.
To make use of it, type the following in your script:

##########################
from onnxcv import ImageClassifier
clf = ImageClassifier(path/to/model)
clf.run()

'''

class ImageClassifier:
    
    def __init__(self, model):

        self.model = model

    def run(self):

        while True:
            # Starting the camera
            cam = cv2.VideoCapture(0)
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Starting the session
            sess = rt.InferenceSession(self.model)

            # Resizing data
            shape = sess.get_inputs()[0].shape
            shape.pop(0)
            shape = tuple(shape)
            X = np.array(img)
            X = resize(X / 255.0, shape)
            X = X[np.newaxis, :, :, :]
            X = X.astype(np.float32)

            # Running the model
            input_name = sess.get_inputs()[0].name
            label_name = sess.get_outputs()[0].name
            pred_onnx = sess.run([label_name], {input_name: X})
            print(pred_onnx)

            # Showing the output
            cv2.imshow('Detect',img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cam.release()
        cv2.destroyAllWindows()