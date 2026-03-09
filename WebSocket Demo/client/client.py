import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello Server")

        response = await websocket.recv()
        print("Server says:", response)

asyncio.run(client())