FROM python:3.11-slim
#робоча директорія – /app
WORKDIR /app
#скопіюйте файл requirements.txt
COPY ./requirements.txt ./requirements.txt
#встановіть потрібні бібліотеки
RUN pip install -r requirements.txt
#скопіюйте увесь код
COPY ./ ./
#вкажіть LOGIN=student123
ENV LOGIN=student123
#запустіть основний файл
CMD ["python3", "-u", "practice.py"]
