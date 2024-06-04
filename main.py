import asyncio
import tornado

from apps import prediction

def make_app():
    handlers = [
        ("/predict", prediction.PredictionHandler)
    ]
    return tornado.web.Application(handlers)

async def main():
    app = make_app()
    app.listen(8000)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())