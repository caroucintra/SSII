from enum import Enum


class Message_type(Enum):
    Correct = 1
    Duplicate_Nonce = 2
    Different_Hash = 3
