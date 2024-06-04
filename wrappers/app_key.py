import os
import uuid
import json

from tornado import web

def require__app_key(func):
    def inner(self: web.RedirectHandler, *args, **kwargs):
        env_key = os.environ.get("APP_KEY", f"{uuid.uuid4()}")
        key = self.request.headers.get('APP-KEY')
        if env_key == key:
            return func(self, *args, **kwargs)
        self.set_status(403)
        self.finish(json.dumps({"message": "Forbidden"}))
    return inner
