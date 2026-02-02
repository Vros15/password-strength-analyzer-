
def estimate_crack_time(entropy_bits: float, guesses_per_second: int) -> float:
    """
    Estimate crack time in seconds based on entropy and guess rate.
    """
    if entropy_bits <= 0:
        return 0.0

    return (2 ** entropy_bits) / guesses_per_second
