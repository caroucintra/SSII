class Message:
    def __init__(self, account_origin, account_destination, amount):
        self._account_origin = account_origin
        self._account_destination = account_destination
        self._amount = amount

    def add_mac(self, mac):
        self._mac = mac

    def add_nonce(self, nonce):
        self._nonce = nonce

    def string_entire_message(self):
        return (
            self._account_origin
            + self._account_destination
            + self._amount
            + self._nonce
        )

    def get_mac(self):
        return self._mac

    def get_nonce(self):
        return self._nonce

    def get_amount(self):
        return self._amount

    def get_account_origin(self):
        return self._account_origin

    def get_account_destination(self):
        return self._account_destination

    def print(self):
        print(
            "From "
            + self._account_origin
            + " to "
            + self._account_destination
            + " amount: "
            + str(self._amount)
        )