#redis i python
from redis import Redis

#connect
host = "localhost"
port = 6379

#connect
server = Redis(
    host="localhost",
    port=6379,
    db=0, # number(index) of database
    decode_responses=True  # decode responses from redis to string
)

# server.set("name", "Alina")
# user_name =server.get("name")
# print(user_name)
# server.set("age", 25)
# age = server.get("age")
# print(age)
# server.set("city", "Kyiv")
# city = server.get("city")
# print(city)
#
# server.set("name", "John")
# user_name = server.get("name")
# print(user_name)
# server.set("age", 30)
# age = server.get("age")
# print(age)
# server.set("city", "London")
# city = server.get("city")
# print(city)

# server.rpush("fruits", "apple", "banana", "orange")
# fruits = server.lrange("fruits", 0, -1)
# print(fruits)
#
# server.hset("user:1", "name", "Alice")
# server.hset("user:1", "age", 25)
# user = server.hgetall("user:1")
# print(user)

# server.sadd("tags", "red", "green", "blue")
# tags = server.smembers("tags")
# print(tags)

# server.incr("counter")
# counter = server.get("counter")
# print(counter)

# server.delete("name")
# name = server.get("name")
# print(name)
# print(bool(server.exists("name")))

# server.setex("message", 60, "Hello, Redis!")
# message = server.get("message")
# print(message)

# server.flushall()
# server.geoadd("geo_locations", (22.2879, 48.6208, "Uzhhorod"))
# location_1 =server.zrange("geo_locations", 0, -1)
# print(location_1)
# server.geoadd("geo_locations", (50.45, 30.52, "Kyiv"))
# location_2 = server.zrange("geo_locations", 0, -1)
# print(location_2)
# dist = server.geodist("geo_locations", "Uzhhorod", "Kyiv", "km")
# print(f"From Uzhhorod to Kyiv {dist} km")

# server.hset("students", "John", 10)
# server.hset("students", "Anna", 9)
# server.hset("students", "Mary", 10)
# server.hset("students", "Dan", 11)
# students = server.hgetall("students")
# print(students)

# server.hset("students", "Anna", 8)
# students = server.hgetall("students")
# print(students)

# server.flushall()
