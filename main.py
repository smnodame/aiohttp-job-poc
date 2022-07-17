from aiohttp import web
import requests
import asyncio

async def function(start_event, end_event):
    # Waits until we get the start event command.
    await start_event.wait()

    # Run our function until we get the end_event being set to true.
    index = 0
    while not end_event.is_set():
        print(f"Function running; index {index}.")
        await asyncio.sleep(2)
        index += 1
        
async def health(request):
    return web.Response(text="<h1> Async Rest API using aiohttp : Health OK </h1>",
                        content_type='text/html')

@asyncio.coroutine
def periodic():
    while True:
        print('periodic')
        yield from asyncio.sleep(30)

async def init():
    app = web.Application()
    app.router.add_get("/", health)

    loop = asyncio.get_event_loop()
    task = loop.create_task(periodic())
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, port=8000)