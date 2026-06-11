# Завдання 1
# Створіть додаток «Соціальна мережа», який зберігає
# інформацію про користувача, його друзів, публікації користувача. Можливості додатку:


# info:user:anton:friends - example
# інформація про користувача імʼя вік місто
#personal_info:{user_name} -- dictionary {"name": "Alina", "age":33}
# хто кому друг
#friends:{user_name} -- set
# публікації
# story:{user_name}:{story_name} -- str
# логіни та паролі
#credential:{user_name} -- str(password)

from redis import Redis

from PythonProject_lesson_32_pickle.practic import friends


class SocialApp:

    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,  # number(index) of database
            decode_responses=True  # decode responses from redis to string
        )

        # user is registered at the moment
        self.current_user = None

        # get keys for DB
    def _get_cred_key(self, user_name):
        return f"credential:{user_name}"

    def _get_personal_info_key(self, user_name):
        return f"personal_info:{user_name}"

    def _get_friends_key(self, user_name):
        return f"friends:{user_name}"

    def _get_story_name_key(self, user_name, story_name):
        return f"story:{user_name}:{story_name}"


# ■ вхід за логіном і паролем;

    def login(self, user_name, password):
        key = self._get_cred_key(user_name)

        #check if user exists
        if not self.server.exists(key):
            print("User doesn't exists")
            return

        #get password from DB and validate:
        true_password = self.server.get(key)

        if true_password != password:
            print("Password is wrong")
            return

        self.current_user = user_name
        print("You are logged in")

    def signup(self, user_name, password):
        key = self._get_cred_key(user_name)

        #check if user already exists
        if self.server.exists(key):
            print(f"User with login {user_name} already exists")
            return

        # add user (login, password) to DB
        self.server.set(key, password)
        print("User is registered")

    # ■ додати користувача;
    # ■ редагувати інформацію про користувача;
    def add_info(self, name, age, city):
        # check if user is logged in:
        if self.current_user is None:
            print("You are not logged in")
            return


        key = self._get_personal_info_key(self.current_user) # get info of user that logged in

        data = {
            "name": name,
            "age": age,
            "city": city
        }

        self.server.hmset(key, data)
        print("Data added")


# ■ видалити користувача;

# ■ пошук користувача за ПІБ;

# ■ перегляд інформації про користувача;

    def get_info(self):
        if self.current_user is None:
            print("You are not logged in")
            return

        key = self._get_personal_info_key(self.current_user)

        data = self.server.hgetall(key)

        print(f"Your data: {data}")

# ■ перегляд усіх друзів користувача;

    def add_friend(self, friend):
        if self.current_user is None:
            print("You are not logged in")
            return

        #check if friend exists (if password exists in DB for friend)
        friend_key = self._get_cred_key(friend)

        if not self.server.exists(friend_key):
            print("Friend doesn't exist")
            return

        # add friend
        key = self._get_friends_key(self.current_user)
        self.server.sadd(key, friend)

        #add my user to friend
        friend_key = self._get_friends_key(friend)
        self.server.sadd(friend_key, self.current_user)

        print("Friend was added")

    def get_friends(self):
        if self.current_user is None:
            print("You are not logged in")
            return

        key = self._get_friends_key(self.current_user)
        friends = self.server.smembers(key)

        print(f"Your friend: {friends}")


# ■ перегляд усіх публікацій користувача.

    def add_story(self, story_name, content):
        if self.current_user is None:
            print("You are not logged in")
            return

        key = self._get_story_key(self.current_user, story_name)

        #check if story exists
        if self.server.exists(key):
            print(f"This story {story_name} exists")
            return

        self.server.set(key, content)

app = SocialApp()

# app.signup("John", "Qwerty2")

app.login("Alina","Qwerty")
# app.add_info(name="Alina Hurtova", age =33, city = "Dnipro")
app.get_info()
app.add_friend("Max")
