import time
import random

while True:
    # every 2 sec print random number
    time.sleep(2)
    print(random.randint(1, 100))

#створення образу - не запущена версія
#docker build -t [назва образу] [шлях до Dockerfile]

# образ створився
# docker images:
# IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
# hello-world:latest   f9078146db2e       22.6kB         10.3kB    U
# my-app:latest        ccc9ae5653d8        212MB         45.7MB
# random_num:latest    4186223f5d53        212MB         45.7MB

# заранити докер - створити контейнер (скільки завгодно можемо)
# docker run -d --name [назва контейнера] [назва образу] # якщо хочемо назвати контейнер
# docker run myapp просто заранити контейнер
# створиться айді # ex. bc394efbab92f27e4267a8788583a87bffceb718cd1e3532109e9f9088d59a74

# docker ps подивитися на контейнер
# CONTAINER ID   IMAGE        COMMAND             CREATED              STATUS              PORTS     NAMES
# bc394efbab92   random_num   "python3 file.py"   About a minute ago   Up About a minute             random

# docker logs [назва контейнера] подивитися на логи - що робить контейнер
