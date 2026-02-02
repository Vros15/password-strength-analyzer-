"""
entropy.py

Estimates password entropy in bits based on character pool size
and password length.
"""
import math


def calculate_entropy(password: str) -> float:
    """
    Estimates password entropy in bits.
    """
    if not password:
        return 0.0

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(not c.isalnum() for c in password):
        pool_size += 32  # approximate symbol count

    if pool_size == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)
