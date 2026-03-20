from sanic import Sanic
from sanic.response import text

app = Sanic("MyApp")

@app.get("/")
async def hello(request):
    return text("Hello Sanic")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, dev=True)