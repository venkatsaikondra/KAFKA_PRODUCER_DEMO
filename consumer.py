from kafka import KafkaConsumer
import json
if __name__=="__main__":
    consumer=KafkaConsumer(
        "consumerdemo",bootstrap_servers="127.0.0.1:9092",auto_offset_reset='earliest',
        group_id="consumer-group-b"
    )
    print("Starting the consumer")
    for msg in consumer:
        print("Registered user={}".format(json.loads(msg.value)))