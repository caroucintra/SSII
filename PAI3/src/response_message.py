class Response_Message:
    def __init__(self, is_integrate, is_correct_nonce, auth_check):
        self._is_integrate = is_integrate
        self._is_correct_nonce = is_correct_nonce
        self._auth_check = auth_check

    def is_integrate(self):
        return self._is_integrate

    def is_correct_nonce(self):
        return self.is_correct_nonce

    def print(self):
        msg = ("Authentication worked: "
            + str(self._auth_check)
            + "Message was stored: "
            + str(self._auth_check)
            + "Message is integrate: "
            + str(self._is_integrate)
            + "\nNonce is unique: "
            + str(self._is_correct_nonce))
        print(msg)
        return msg
