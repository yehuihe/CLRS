"""Custom warnings and errors used across CLRS."""


__all__ = [
    "StackUnderflowError",
    "StackOverflowError",
]


class StackUnderflowError(Exception):
    """Exception class to raise if we attempt to pop an empty stack.

    This class inherits from Exception to help with
    exception handling and backward compatibility.

    Examples
    --------
    # TODO: add examples

    """


class StackOverflowError(Exception):
    """Exception class to raise if stack S.top exceeds length of stack n.

    This class inherits from both Exception to help with
    exception handling and backward compatibility.

    Examples
    --------
    # TODO: add examples

    """
