from enum import Enum


class ExtendedEnum(str, Enum):
    @classmethod
    def list_members(cls):
        return [c for c in cls]

    @classmethod
    def list_values(cls):
        return list(map(lambda c: c.value, cls))

    @property
    def values(self):
        return self.list_values()
