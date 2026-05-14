#python version
FROM python:3.11-slim

#create folder
WORKDIR /app

#copy requirements and libs  pip freeze > requirements.txt
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# cpoy all files
COPY ./ ./

# run
CMD ["python3", "-u", "main.py"]
