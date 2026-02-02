
def estimate_crack_time(entropy_bits: float, guesses_per_second: int) -> float:
    """
    Estimate crack time in seconds based on entropy and guess rate.
    """
    if entropy_bits <= 0:
        return 0.0

    return (2 ** entropy_bits) / guesses_per_second

def format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.1f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.1f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.1f} days"
    else:
        return f"{seconds / 31536000:.1f} years"
