import asyncio
import tornado

from apps import prediction

def make_app():
    handlers = [
        ("/predict", prediction.PredictionHandler)
    ]
    return tornado.web.Application(handlers)

app = make_app()

async def main():
    app.listen(8001)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())