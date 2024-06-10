import os

import cv2
import numpy as np

MEDIA = os.environ["MEDIA_DIR"]

def model_predict(model, request_body):
    images = request_body.get("images")
    def data_generator():
        for image_name in images:
            image_path = os.path.join(MEDIA, image_name)
            image_ = cv2.imread(image_path)
            image_ = cv2.resize(image_, (224, 224))
            image_ = np.expand_dims(image_, axis=0)
            yield image_

    data_iterator = iter(data_generator())
    predictions = []
    while (sample := next(data_iterator, None)) is not None:
        sample_prediction = model.predict(sample)
        predictions.append(sample_prediction[0][0])
    return sum(predictions)/len(predictions)
