class Response_Message:
    def __init__(self, is_integrate, is_correct_nonce):
        self._is_integrate = is_integrate
        self._is_correct_nonce = is_correct_nonce

    def is_integrate(self):
        return self._is_integrate

    def is_correct_nonce(self):
        return self.is_correct_nonce

    def print(self):
        print(
            "Message is integrate: "
            + str(self._is_integrate)
            + "\nNonce is unique: "
            + str(self._is_correct_nonce)
        )
