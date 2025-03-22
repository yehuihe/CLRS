import math

import numpy as np


# TODO: memory profile for strassen and strassen2


def max_subarray_brute_force(A):
    """The maximum-subarray problem brute force algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    low : int
        Left index demarcating a maximum subarray.

    high : int
        Right index demarcating a maximum subarray.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the maximum subarray problem brute force algorithm is:

    >>> A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    >>> max_subarray_brute_force(A)
    (7, 10)
-
    """
    max_so_far = -math.inf
    for l in range(len(A)):
        sum = 0
        for h in range(l, len(A)):
            sum += A[h]
            if sum > max_so_far:
                max_so_far = sum
                low = l
                high = h
    return low, high


def _find_max_crossing_subarray(A, low, mid, high):
    """The maximum subarray crossing the midpoint.

        Parameters
        ----------
        A : ndarray, shape (n,)
            A sequence of n numbers (a1, a2, ..., an),
            where ``n`` is the number of elements in the sequence.

        low : int
            Left index of array A[low, high].

        mid : int
            Middle index of array A[low, high].

        high : int
            Right index of array A[low, high].

-        Returns
        -------
        max_left : int
            Left index demarcating a maximum subarray.

        max_right : int
            Right index demarcating a maximum subarray.

        sum : int
            The sum of the values in a maximum subarray.

        References
        ----------
        .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
            to Algorithms, Third Edition. 3rd ed., The MIT Press.

        """
    left_sum = -math.inf
    max_left = -math.inf
    max_right = math.inf
    sum = 0
    for i in range(mid, low, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -math.inf
    sum = 0
    for j in range(mid + 1, high):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    """The maximum-subarray problem brute force algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    low : int
        Left index of array A[low, high].

    high : int
        Right index of array A[low, high].

    Returns
    -------
    low : int
        Left index demarcating a maximum subarray.

    high : int
        Right index demarcating a maximum subarray.

    sum : int
        The sum of the values in a maximum subarray.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the find maximum subarray algorithm is:

    >>> A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    >>> find_maximum_subarray(A, 0, len(A)-1)
    (7, 10, 43)

    """
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = _find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def max_subarray_linear(A):
    """The maximum-subarray problem linear-time algorithm.

    Parameters
    ----------
    A : ndarray, shape (n,)
        A sequence of n numbers (a1, a2, ..., an),
        where ``n`` is the number of elements in the sequence.

    Returns
    -------
    low : int
        Left index demarcating a maximum subarray.

    high : int
        Right index demarcating a maximum subarray.

    max_sum : int
        The sum of the values in a maximum subarray.

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the maximum subarray linear algorithm is:

    >>> A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    >>> max_subarray_linear(A)
    (7, 10, 43)

    """
    max_sum = -math.inf
    ending_here_sum = -math.inf
    for j in range(len(A)-1):
        ending_here_high = j
        if ending_here_sum > 0:
            ending_here_sum += A[j]
        else:
            ending_here_low = j
            ending_here_sum = A[j]
        if ending_here_sum > max_sum:
            max_sum = ending_here_sum
            low = ending_here_low
            high = ending_here_high

    return low, high, max_sum


def square_matrix_multiply(A, B):
    """Naive square matrix multiplication algorithm.

    # TODO: parameter varification: square matrix

    Parameters
    ----------
    A : (N, N) array_like
        Left matrix to multiply.

    B : (N, N) array_like
        Right matrix to multiply.

    Returns
    -------
    C : (N, N) array_like
        Product of A and B

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the square matrix multiply algorithm is:

    >>> A = np.array([[0., 1.,],
    ...               [0., 0.]])
    >>> B = np.array([[0., 0.,],
    ...               [1., 0.]])
    >>> square_matrix_multiply(A, B)
    array([[1., 0.],
           [0., 0.]])
    >>> square_matrix_multiply(B, A)
    array([[0., 0.],
           [0., 1.]])

    Another example.

    >>> A = np.array([[2., -3.,],
    ...               [-1., 5.]])
    >>> B = np.array([[13., 9.,],
    ...               [4., 0.]])
    >>> square_matrix_multiply(A, B)
    array([[14., 18.],
           [ 7., -9.]])

    """
    n = A.shape[0]
    C = np.zeros_like(A)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]

    return C


def square_matrix_multiply_recursive(A, B):
    """Recursive square matrix multiplication algorithm.

    # TODO: parameter varification: square matrix; we assume that n is an exact power of 2 in each of

    Parameters
    ----------
    A : (N, N) array_like
        Left matrix to multiply.

    B : (N, N) array_like
        Right matrix to multiply.

    Returns
    -------
    C : (N, N) array_like
        Product of A and B

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the recursive square matrix multiply algorithm is:

    >>> A = np.array([[2., -3.,],
    ...               [-1., 5.]])
    >>> B = np.array([[13., 9.,],
    ...               [4., 0.]])
    >>> square_matrix_multiply_recursive(A, B)
    array([[14., 18.],
           [ 7., -9.]])

    """

    n = A.shape[0]
    C = np.empty_like(A)
    if n == 1:
        return A[0, 0] * B[0, 0]
    else:
        # Index calculations. We identify a submatrix by a range of
        # row indices and a range of column indices of the original matrix.
        n_half = n // 2
        C_11 = (square_matrix_multiply_recursive(A[:n_half, :n_half], B[:n_half, :n_half])
                + square_matrix_multiply_recursive(A[:n_half, n_half:], B[n_half:, :n_half]))
        C_12 = (square_matrix_multiply_recursive(A[:n_half, :n_half], B[:n_half, n_half:])
                + square_matrix_multiply_recursive(A[:n_half, n_half:], B[n_half:, n_half:]))
        C_21 = (square_matrix_multiply_recursive(A[n_half:, :n_half], B[:n_half, :n_half])
                + square_matrix_multiply_recursive(A[n_half:, n_half:], B[n_half:, :n_half]))
        C_22 = (square_matrix_multiply_recursive(A[n_half:, :n_half], B[:n_half, n_half:])
                + square_matrix_multiply_recursive(A[n_half:, n_half:], B[n_half:, n_half:]))

    # Combine C11, C12, C21, and C22 into C
    C[:n_half, :n_half] = C_11
    C[:n_half, n_half:] = C_12
    C[n_half:, :n_half] = C_21
    C[n_half:, n_half:] = C_22

    return C


def strassen(A, B):
    """Strassen’s algorithm for matrix multiplication.

    # TODO: parameter varification: square matrix; we assume that n is an exact power of 2 in each of

    Parameters
    ----------
    A : (N, N) array_like
        Left matrix to multiply.

    B : (N, N) array_like
        Right matrix to multiply.

    Returns
    -------
    C : (N, N) array_like
        Product of A and B

    References
    ----------
    .. [1] Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction
        to Algorithms, Third Edition. 3rd ed., The MIT Press.

    Examples
    --------
    A simple application of the recursive square matrix multiply algorithm is:

    >>> A = np.array([[2., -3.,],
    ...               [-1., 5.]])
    >>> B = np.array([[13., 9.,],
    ...               [4., 0.]])
    >>> strassen(A, B)
    array([[14., 18.],
           [ 7., -9.]])

    """
    n = A.shape[0]
    C = np.empty_like(A)
    if n == 1:
        return A[0, 0] * B[0, 0]
    else:
        # Partition A and B in equations (4.9)
        # Let C11, C12, C21, and C22 be n/2 * n/2 matrices
        # create n/2 * n/2 matrices S1, S2, ..., S10 and P1, P2, ..., P7
        n_half = n // 2
        S_1 = B[:n_half, n_half:] - B[n_half:, n_half:]
        S_2 = A[:n_half, :n_half] + A[:n_half, n_half:]
        S_3 = A[n_half:, :n_half] + A[n_half:, n_half:]
        S_4 = B[n_half:, :n_half] - B[:n_half, :n_half]
        S_5 = A[:n_half, :n_half] + A[n_half:, n_half:]
        S_6 = B[:n_half, :n_half] + B[n_half:, n_half:]
        S_7 = A[:n_half, n_half:] - A[n_half:, n_half:]
        S_8 = B[n_half:, :n_half] + B[n_half:, n_half:]
        S_9 = A[:n_half, :n_half] - A[n_half:, :n_half]
        S_10 = B[:n_half, :n_half] + B[:n_half, n_half:]

        P_1 = strassen(A[:n_half, :n_half], S_1)
        P_2 = strassen(S_2, B[n_half:, n_half:])
        P_3 = strassen(S_3, B[:n_half, :n_half])
        P_4 = strassen(A[n_half:, n_half:], S_4)
        P_5 = strassen(S_5, S_6)
        P_6 = strassen(S_7, S_8)
        P_7 = strassen(S_9, S_10)

        C_11 = P_5 + P_4 - P_2 + P_6
        C_12 = P_1 + P_2
        C_21 = P_3 + P_4
        C_22 = P_5 + P_1 - P_3 - P_7

        # Combine C11, C12, C21, and C22 into C
        C[:n_half, :n_half] = C_11
        C[:n_half, n_half:] = C_12
        C[n_half:, :n_half] = C_21
        C[n_half:, n_half:] = C_22

    return C




# def strassen2(A, B):
#     n = A.shape[0]
#     C = np.empty_like(A)
#     if n == 1:
#         return A[0, 0] * B[0, 0]
#     else:
#         # Partition A and B in equations (4.9)
#         # Let C11, C12, C21, and C22 be n/2 * n/2 matrices
#         # create n/2 * n/2 matrices S1, S2, ..., S10 and P1, P2, ..., P7
#         n_half = n // 2
#         A_11 = A[:n_half, :n_half]
#         A_12 = A[:n_half, n_half:]
#         A_21 = A[n_half:, :n_half]
#         A_22 = A[n_half:, n_half:]
#         B_11 = B[:n_half, :n_half]
#         B_12 = B[:n_half, n_half:]
#         B_21 = B[n_half:, :n_half]
#         B_22 = B[n_half:, n_half:]
#
#         S_1 = B_12 - B_22
#         S_2 = A_11 + A_12
#         S_3 = A_21 + A_22
#         S_4 = B_21 - B_11
#         S_5 = A_11 + A_22
#         S_6 = B_11 + B_22
#         S_7 = A_12 - A_22
#         S_8 = B_21 + B_22
#         S_9 = A_11 - A_21
#         S_10 = B_11 + B_12
#
#         P_1 = strassen(A_11, S_1)
#         P_2 = strassen(S_2, B_22)
#         P_3 = strassen(S_3, B_11)
#         P_4 = strassen(A_22, S_4)
#         P_5 = strassen(S_5, S_6)
#         P_6 = strassen(S_7, S_8)
#         P_7 = strassen(S_9, S_10)
#
#         C_11 = P_5 + P_4 - P_2 + P_6
#         C_12 = P_1 + P_2
#         C_21 = P_3 + P_4
#         C_22 = P_5 + P_1 - P_3 - P_7
#
#         # Combine C11, C12, C21, and C22 into C
#         C[:n_half, :n_half] = C_11
#         C[:n_half, n_half:] = C_12
#         C[n_half:, :n_half] = C_21
#         C[n_half:, n_half:] = C_22
#
#     return C
