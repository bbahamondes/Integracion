#!/bin/python3
import asyncio
import websockets
import re
import json
from kafka import KafkaConsumer

broker='bbahamondes-2.hwx.com:6667'
consumer = KafkaConsumer("logs",
                        bootstrap_servers=broker,
                        security_protocol='SASL_PLAINTEXT',
                        sasl_mechanism='GSSAPI')

pattern = re.compile('^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\,\d{3}) (?P<level>\w+) \[(?P<component>[()\w\- ./\d]*)\] (?P<body>.*)$')

async def hello(websocket, path):
    while True:
        for msg in consumer:
            msgSend = {}
            val = pattern.match(msg.value.decode('utf-8'))
            for key in val.groupdict().keys():
                msgSend[key] = val[key]
            await websocket.send(json.dumps(msgSend))
            print (msg.value.decode('utf-8'))

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
