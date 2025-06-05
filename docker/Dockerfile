# Используем официальный образ Python в качестве базового
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл требований и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы приложения
COPY . .

# Устанавливаем права на выполнение для скрипта entrypoint
RUN chmod +x ./docker/entrypoint.sh

# Запускаем приложение с использованием скрипта entrypoint
CMD ["/bin/bash", "./docker/entrypoint.sh"]
