from kafka import KafkaProducer
from data import get_random_data
import json
import time
def json_serializer(data):
    return json.dumps(data).encode("utf-8")
producer=KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],value_serializer=json_serializer)
if __name__=="__main__":
    while 1==1:
        registed_user=get_random_data()
        print(registed_user)
        producer.send("consumerdemo",registed_user)
        time.sleep(4)