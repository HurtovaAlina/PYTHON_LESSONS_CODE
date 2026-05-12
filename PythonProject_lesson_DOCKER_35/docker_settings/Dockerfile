FROM python:3.11-slim

# базова папка куди копіювати файли

WORKDIR /app

# скопіювати файли
COPY ./ ./

# встановити бібліотеки
RUN pip install -r requirements.txt

# вказати налаштування (змінні середовища)
ENV MIN_NUM=0


# команди для запуску -u щоб працював print

CMD ["python3", "-u",  "main.py"]
