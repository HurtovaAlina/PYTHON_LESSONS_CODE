FROM python:3.11-slim

WORKDIR app

COPY ./ ./

# pip freeze > requirements.txt  - підтягнути актуальні бібліотеки
RUN pip install -r requirements.txt

EXPOSE 8080

# -u щоб печатвся елемент списку
CMD ["python3", "-u","main.py"]
