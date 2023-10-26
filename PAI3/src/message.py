class Message:
    def __init__(self, username, password, message):
        self._username = username
        self._password = password
        self._message = message

    def add_mac(self, mac):
        self._mac = mac

    def add_nonce(self, nonce):
        self._nonce = nonce

    def string_entire_message(self):
        return (
            self._username
            + self._password
            + self._message
            + self._nonce
        )

    def get_mac(self):
        return self._mac

    def get_nonce(self):
        return self._nonce

    def get_message(self):
        return self._message

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def print(self):
        print(
            "From user: "
            + self._username
            + ", message: "
            + str(self._message)
        )

    def format_data(self):
        return "(" + self._username + self._password + self._message + ")"