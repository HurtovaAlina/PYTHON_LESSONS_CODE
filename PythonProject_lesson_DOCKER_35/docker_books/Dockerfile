FROM python:3.11-slim
#робоча директорія – /app
WORKDIR /app
#скопіюйте файл requirements.txt -> перед docker build виконати pip freeze > requirements.txt
COPY ./requirements.txt ./requirements.txt
#встановіть потрібні бібліотеки
RUN pip install -r requirements.txt
#скопіюйте увесь код
COPY ./ ./
#вкажіть обовʼязково
ENV HOST="0.0.0.0"
ENV PORT=8080

# відкрити порт
EXPOSE 8080

#запустіть основний файл
CMD ["python3", "-u", "main.py"]
