# Kafka Edu Sprint 1

## Используемые технологии:
* Код Python.
* Kafka кластер на базе Kraft
* Запуск через Docker Compose.

## Технические инструкции

### Запуск кластера Kafka 
```bash 
docker compose up -d
```

### Создание топика 
```bash 
docker compose exec kafka-0 kafka-topics.sh --create --topic maintopic --bootstrap-server kafka-0:9092 --partitions 2 --replication-factor 3
```

### Запуск продюсера и консюмеров 
```bash 
docker compose exec app python main.py producer
docker compose exec app python main.py single
docker compose exec app python main.py batch                                  
```

### Остановка сервисов 
```bash 
docker compose down                                
```
