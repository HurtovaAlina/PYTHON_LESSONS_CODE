from redis import Redis
#
# Завдання 2
# Створіть додаток «Музей літератури». Додаток має зберігати
# інформацію про експонати та людей, які мають відношення
# до експонатів. Можливості додатку:

# password:user 1234
# exponat:name description
# people:name description
# exponat:name:people name

# ■ вхід за логіном і паролем;
# ■ додати експонат;
# ■ видалити експонат;
# ■ редагування інформації про експонат;
# ■ перегляд повної інформації про експонат;
# ■ виведення інформації про всі експонати;
# ■ перегляд інформації про людей, які мають відношення
# до певного експонату;
# ■ перегляд інформації про експонати, що мають відношення
# до певної людини;
# ■ перегляд набору експонатів на основі певного критерію.
# Наприклад, показати всі книжкові експонати.

class Museum:

    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,  # number(index) of database
            decode_responses=True  # decode responses from redis to string
        )

# user is registered at the moment
        self.is_loggedin = False

        # get keys for DB
    def _get_password_key(self, user_name):
        return f"password:{user_name}"

    def _get_exponat_key(self, name):
        return f"exponat:{name}"

    def _get_people_key(self, name):
        return f"people: {name}"

    def _get_exponat_people_key(self, exponat_name):
        return f"exponat:{exponat_name}:people"


# registration
    def signup(self, user_name, password):
        key = self._get_password_key(user_name)

        #check if user already exists
        if self.server.exists(key):
            print(f"User with login {user_name} already exists")
            return

        # add user (login, password) to DB
        self.server.set(key, password)
        print("User is registered")

# ■ вхід за логіном і паролем;

    def login(self, user_name, password):
        key = self._get_password_key(user_name)

        #check if user exists
        if not self.server.exists(key):
            print("User doesn't exists")
            return

        #get password from DB and validate:
        true_password = self.server.get(key)

        if true_password != password:
            print("Password is wrong")
            return

        self.is_loggedin = True

        print("You are logged in")

    # ■ додати експонат;
    def add_exponat(self, name, description):
        if not self.is_loggedin:
            print("You are not logged in")
            return

        key = self._get_exponat_key(name)

        self.server.set(key, description)


museum = Museum()

# museum.signup("Alina", "1234")
museum.login("Alina", "1234")
museum.add_exponat("book", "dictionary")
museum.add_exponat("book2", "medicine")
