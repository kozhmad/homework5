# Базовый образ, содержащий Python
FROM python:3.9-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копируем все файлы программы в контейнер
COPY . /app

# Установка зависимостей (если у вас есть файл requirements.txt)
# Если зависимостей нет, пропустите
# RUN pip install -r requirements.txt

# Указываем команду для запуска приложения
ENTRYPOINT ["python", "main.py"]