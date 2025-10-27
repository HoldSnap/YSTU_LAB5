# Layered Architecture Lab

## Описание
Лабораторная работа по теме: **Слоистая архитектура с PostgreSQL**

## Запуск
1. Поднять базу данных:
```bash
docker compose up -d db
```

2. Установить зависимости:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Запустить приложение:
```bash
python app.py
```

4. Проверить работу API:
```bash
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name":"Иван","email":"ivan@example.com"}'
curl http://localhost:5000/users
```

5. Прогнать тесты:
```bash
pytest -v
```
