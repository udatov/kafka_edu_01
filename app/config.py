from pydantic_settings import BaseSettings
from typing import List


class KafkaSettings(BaseSettings):
    
    bootstrap_servers: str = 'kafka-0:9092'
    topic: str = 'maintopic'
    partitions: int = 3
    replication_factor: int = 2
    producer_acks: str = 'all'
    producer_retries: int = 5
    group_id_single: str = 'single-message-group'
    group_id_batch: str = 'batch-message-group'
    enable_auto_commit_single: bool = True
    enable_auto_commit_batch: bool = False
    auto_offset_reset: str = 'earliest'
    fetch_min_bytes: int = 1024
    fetch_max_wait_ms: int = 500
    consumer_timeout_ms: int = 1000
    msg_number: int = 50
    
    class Config:
        env_file = '.env'

kafka_settings = KafkaSettings()
