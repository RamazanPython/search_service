from enum import Enum


class Choice(Enum):
    @classmethod
    def choices(cls):
        return [(c.value, c.name) for c in cls]

    @classmethod
    def repr(cls):
        return {c.name: {'id': c.value, 'name': c.name} for c in cls}

    @classmethod
    def list(cls):
        return [c.value for c in cls]

    def __str__(self):
        return self.value


class SearchDataStatusChoice(str, Choice):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    NO_DATA = 'NO_DATA'
    FAILED = 'FAILED'


class CurrencyCodeChoice(str, Choice):
    KZT = 'KZT'
