#!/bin/bash

# Запуск основного приложения
echo "Starting the recommendation system..."
python app/main.py &

# Запуск веб-сервера для визуализации
echo "Starting the web server for visualization..."
nginx -g "daemon off;"
