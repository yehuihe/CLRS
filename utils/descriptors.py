"""Descriptors utilities within CLRS."""


# Authors: Yehui He

# License: BSD 3 clause


class ReadOnly:
    """Generic Read-only descriptor for class attributes."""

    def __init__(self):
        self._name = None

    def __set_name__(self, owner, name):
        self.name = name
        self._name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if self._name in instance.__dict__:
            raise AttributeError(f"Can't set attribute {self.name!r}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError(f"Can't delete attribute {self._name!r}")
