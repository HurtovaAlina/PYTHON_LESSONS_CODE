FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

#host 0.0.0.0 own PC address
ENV HOST="0.0.0.0"
#port
ENV PORT=8080
#open port for user
EXPOSE 8080
# run
CMD ["python", "main.py"]
