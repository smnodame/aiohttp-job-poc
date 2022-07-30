from aiohttp import web
import requests
import asyncio
from sklearn import tree

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

    # [พัดลม, ทีวี, microwave]

    # X = [[0, 0], [1,1]]
    X = [
        [0, 0, 0], 
        [0, 0, 1], 
        [0, 1, 0], 
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]

    Y = [
        'ไม่อยู่',
        'ทำอาหาร',
        'ดูทีวี',
        'ดูทีวี',
        'นอนเล่น',
        'นอนเล่น',
        'นอนเล่น',
        'นอนเล่น'
    ]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    print('===========')
    # r = export_text(clf, feature_names=['พัดลม', 'ทีวี', 'microwave'])
    # print(r)
    print('======xx=====')
    print(clf.predict([[1, 1, 1]]))

    loop = asyncio.get_event_loop()
    task = loop.create_task(periodic())
    return app


if __name__ == "__main__":
    application = init()
    web.run_app(application, port=8000)