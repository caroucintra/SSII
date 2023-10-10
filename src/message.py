class Message:
    def __init__(self, account_origin, account_destination, amount):
        self._account_origin = account_origin
        self._account_destination = account_destination
        self._amount = amount

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
