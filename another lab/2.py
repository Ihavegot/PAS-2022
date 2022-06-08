# ws://echo.websocket.events

import asyncio
import websockets


async def handshake():
    async with websockets.connect('ws://echo.websocket.events:80') as wsocket:
        print("Hand shaked")
        await wsocket.send("Hello world!")
        message = await wsocket.recv()

        print(message)


asyncio.run(handshake())
