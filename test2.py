#!./bin/python
from kafka import KafkaConsumer
from datetime import datetime as dt
 
broker='bbahamondes-2.hwx.com:6667'
 
# point ssl lib to a certificate file that will work for your Kafka cluster
# ssl_context = ssl.create_default_context(cafile='/etc/pki/tls/certs/ca-bundle.crt')
 
consumer = KafkaConsumer("logs",
                        bootstrap_servers=broker,
                        security_protocol='SASL_PLAINTEXT',
                        sasl_mechanism='GSSAPI')
#producer = KafkaProducer(bootstrap_servers=broker,
#                        security_protocol='SASL_SSL',
#                        sasl_mechanism='GSSAPI',
#                        ssl_context=ssl_context)
#msg = f'test-{dt.utcnow().isoformat()}'
#meta = producer.send(topic='some-topic', value=msg.encode('utf-8'))
#ConsumerRecord(topic='logs', partition=0, offset=94403, timestamp=1584190310718, timestamp_type=0, key=None, value=b'2020-03-14 12:51:50,507 INFO [pool-14-thread-1] o.a.n.c.r.WriteAheadFlowFileRepository Successfully checkpointed FlowFile Repository with 30826 records in 1481 milliseconds', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=172, serialized_header_size=-1)
for msg in consumer:
    print (str(msg.value))