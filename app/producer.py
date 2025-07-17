from confluent_kafka import Producer
from message import Format
from config import kafka_settings
import time
import logging

logging.basicConfig(level=logging.INFO)


def acked(err, msg):
    if err is not None:
        logging.error(f"Message failed delivery: {err}")
    else:
        logging.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def run_producer():
    p = Producer({
        "bootstrap.servers": kafka_settings.bootstrap_servers,
        "acks": kafka_settings.producer_acks,
        "retries": kafka_settings.producer_retries,
    })
    for i in range(kafka_settings.msg_number):
        msg = Format(f"key-{i}", f"value-{i}")
        try:
            logging.info(f"Producer sending: {msg.to_json()}")
            p.produce(
                kafka_settings.topic,
                key=msg.key.encode("utf-8"),
                value=msg.to_json().encode("utf-8"),
                callback=acked
            )
        except Exception as e:
            logging.error(f"Producer ERROR: {e}")

        p.poll(0)
        time.sleep(0.5)
    p.flush()
