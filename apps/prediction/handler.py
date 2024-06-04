from tornado import web, escape

from wrappers import require__app_key, require__json_body
from processor import model_predict
from tf_model import tf_model

class PredictionHandler(web.RequestHandler):
    @require__app_key
    @require__json_body
    def post(self):
        request_body = escape.json_decode(self.request.body)
        prediction_result = model_predict(tf_model.get_model(), request_body)
        self.write({"result": prediction_result})
