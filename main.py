import os

import logging
import asyncio
import tornado

from apps import prediction

PORT = int(os.environ["WEB_MODEL_PORT", "8001"])

logger = logging.getLogger("MODEL")

def make_app():
    handlers = [
        ("/predict", prediction.PredictionHandler)
    ]
    return tornado.web.Application(handlers)

app = make_app()

async def main():
    app = make_app()
    app.listen(PORT)
    logger.info(f"Server started on port {PORT}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())