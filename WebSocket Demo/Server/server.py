import asyncio
import websockets

async def server(websocket):
    print("Client connected")

    async for message in websocket:
        print("Received:", message)

        reply = "Server received: " + message
        await websocket.send(reply)

async def main():
    async with websockets.serve(server, "localhost", 8765):
        print("Server running at ws://localhost:8765")
        await asyncio.Future()   # keep server running

asyncio.run(main())