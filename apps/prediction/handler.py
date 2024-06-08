from tornado import web, escape
import logging

from wrappers import require__app_key, require__json_body
from processor import model_predict
from tf_model import tf_model

logger = logging.getLogger("[Prediction]")


class PredictionHandler(web.RequestHandler):
    @require__app_key
    @require__json_body
    def post(self):
        request_body = escape.json_decode(self.request.body)
        prediction_result = model_predict(tf_model.get_model(), request_body)
        logger.log(logging.INFO, "{prediction_result}")
        self.write({"result": prediction_result})
