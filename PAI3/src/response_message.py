class Response_Message:
    def __init__(self, is_integrate, is_correct_nonce, check_auth):
        self._is_integrate = is_integrate
        self._is_correct_nonce = is_correct_nonce
        self._check_auth = check_auth

    def check_auth(self):
        return self._check_auth
    
    def is_integrate(self):
        return self._is_integrate

    def is_correct_nonce(self):
        return self.is_correct_nonce

    def print(self):
        msg = ("Authentication worked: "
            + str(self._check_auth)
            + "\nMessage is integrate: "
            + str(self._is_integrate)
            + "\nNonce is unique: "
            + str(self._is_correct_nonce))
        print(msg)
        return msg
