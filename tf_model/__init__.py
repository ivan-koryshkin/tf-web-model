import os
import tensorflow as tf

import config

path = os.environ["KERAS_MODEL_PATH"]

class TFModel:
    def __init__(self) -> None:
        self._model = None
    
    def get_model(self):
        if not self._model:
           print("Load model:", path)
           self._model = tf.keras.models.load_model(
               path, 
               custom_objects=config.MODEL_CUSTOM_LAYERS
            )
        return self._model


tf_model = TFModel()