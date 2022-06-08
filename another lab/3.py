# ws://echo.websocket.events

import asyncio
import websockets

async def handshake():
    async with websockets.connect('ws://echo.websocket.events:80') as wsocket:
        print("Hand shaked")

        await wsocket.send(input("Type your message\n> "))
        message = await wsocket.recv()

        print(message)

asyncio.run(handshake())