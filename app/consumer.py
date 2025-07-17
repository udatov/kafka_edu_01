from confluent_kafka import Consumer, KafkaException
from message import Format
from config import kafka_settings
import json
import logging

logging.basicConfig(level=logging.INFO)


def run_consumer_single():
    c = Consumer({
        "bootstrap.servers": kafka_settings.bootstrap_servers,
        "group.id": kafka_settings.group_id_single,
        "auto.offset.reset": kafka_settings.auto_offset_reset,
        "enable.auto.commit": True,
    })
    c.subscribe([kafka_settings.topic])
    logging.info("Single Consumer started...")
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                logging.error(f"Consumer error: {msg.error()}")
                continue
            try:
                m = Format.from_json(msg.value().decode("utf-8"))
                logging.info(f"SINGLE: {m.to_json()}")
            except Exception as err:
                logging.error(f"Single consumer deserialization error: {err}")
    except KeyboardInterrupt:
        pass
    finally:
        c.close()


def run_consumer_batch():
    c = Consumer({
        "bootstrap.servers": kafka_settings.bootstrap_servers,
        "group.id": kafka_settings.group_id_batch,
        "auto.offset.reset": kafka_settings.auto_offset_reset,
        "enable.auto.commit": False,
        "fetch.min.bytes": kafka_settings.fetch_min_bytes,
        "fetch.wait.max.ms": kafka_settings.fetch_max_wait_ms
    })
    c.subscribe([kafka_settings.topic])
    logging.info("Batch Consumer started...")
    try:
        while True:
            msgs = c.consume(num_messages=10, timeout=1.0)
            if not msgs:
                continue
            for msg in msgs:
                if msg.error():
                    logging.error(f"Batch consumer error: {msg.error()}")
                    continue
                try:
                    m = Format.from_json(msg.value().decode("utf-8"))
                    logging.info(f"BATCH: {m.to_json()}")
                except Exception as err:
                    logging.error(f"Batch deserialization error: {err}")
            try:
                c.commit(asynchronous=False)
            except KafkaException as ke:
                logging.error(f"Batch consumer commit error: {ke}")
    except KeyboardInterrupt:
        pass
    finally:
        c.close()
