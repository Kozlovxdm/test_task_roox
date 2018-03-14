**Запуск Docker**
docker-compose up -d
docker ps
docker cp db.sql container_name:/
docker exec -it container_name /bin/bash
psql -h localhost -U dimon dimon < db.sql

**Установка Python3, создание виртуальной среды**
sudo apt-get install python3, python3-dev, pip3
pip3 install virtualenv
virtualenv -p python3 --prompt=" (server) " env
source env/bin/activate
pip install -r requirements.txt

**Запуск сервера, запуск тестов**
python server.py
python tests.py
