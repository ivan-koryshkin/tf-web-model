import json

from tornado import web, escape


def require__json_body(func):
    def inner(self: web.RedirectHandler, *args, **kwargs):
        if self.request.body:
            try:
                escape.json_decode(self.request.body)
                return func(self, *args, **kwargs)
            except json.decoder.JSONDecodeError:
                pass
        self.set_status(422)
        self.finish(json.dumps({"message": "JSON decode error"}))
    return inner