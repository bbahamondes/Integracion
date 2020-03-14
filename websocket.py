import asyncio
import websockets
from kafka import KafkaConsumer

broker='bbahamondes-2.hwx.com:6667'
consumer = KafkaConsumer("logs",
                        bootstrap_servers=broker,
                        security_protocol='SASL_PLAINTEXT',
                        sasl_mechanism='GSSAPI')

async def hello(websocket, path):
    while True:
        for msg in consumer:
            await websocket.send(str(msg.value))
            print (msg.value)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
