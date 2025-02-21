import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def save_to_file(username, password):
    with open("user_details.txt", "a") as file:
        file.write(f'{username},{hash_password(password.encode('utf-8'))}\n')

def register_user(username, password):
    while True:
        username = input("Enter username: ")
        if not username:
            print("Username can't be empty")
            continue
        break

    while True:
        password = input("Enter password: ")
        if not password:
            print("Password can't be empty")
            continue
        break

    save_to_file(username, password)


    def main():
        menu = """
        1. to register_user
        2. to login username
        3. to exit:  """

        choice = input(menu)

