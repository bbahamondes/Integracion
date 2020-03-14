import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(f"< {greeting}")

while True:
    asyncio.get_event_loop().run_until_complete(hello()) #run_until_complete(hello())
asyncio.get_event_loop().run_forever()