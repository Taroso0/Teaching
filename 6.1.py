class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно изменён.")

    def check_password(self, password):
        return self.__password == password

user_account = UserAccount("john_doe", "john@example.com", "securepassword123")

user_account.set_password("new_securepassword456")

is_correct = user_account.check_password("new_securepassword456")
print("Пароль верен:", is_correct)

is_correct = user_account.check_password("wrongpassword")
print("Пароль верен:", is_correct)