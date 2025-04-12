"""Custom warnings and errors used across CLRS."""


__all__ = [
    "StackUnderflowError",
    "StackOverflowError",
    "QueueUnderflowError",
    "QueueOverflowError",
    "HeapUnderflowError",
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


class QueueUnderflowError(Exception):
    """Exception class to raise if we attempt to dequeue an element from an empty queue

    This class inherits from Exception to help with
    exception handling and backward compatibility.

    Examples
    --------
    # TODO: add examples

    """


class QueueOverflowError(Exception):
    """Exception class to raise if the queue is full,
    and if we attempt to enqueue an
    element

    This class inherits from both Exception to help with
    exception handling and backward compatibility.

    Examples
    --------
    # TODO: add examples

    """


class HeapUnderflowError(Exception):
    """Exception class to raise if the Heap underflow.

    This class inherits from both Exception to help with
    exception handling and backward compatibility.

    Examples
    --------
    # TODO: add examples

    """