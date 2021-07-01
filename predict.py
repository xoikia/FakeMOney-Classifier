import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image

class fakeclf:
    def __init__(self,filename):
        self.filename =filename


    def predictionfakenote(self):
        # load model
        model = load_model('FakeNoteClf.h5')

        label=['Fake 200', 'Real 200', 'Fake 500', 'Real 500']

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        prediction=label[np.argmax(result)]

        return [{"image":prediction}]