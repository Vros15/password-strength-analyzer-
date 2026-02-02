"""
scorer.py

Aggregates password evaluation rules and produces a final score.
"""

from analyzer.entropy import calculate_entropy
from analyzer.crack_time import estimate_crack_time
from analyzer.rules import (
    length_rule,
    character_variety_rule,
    repeated_characters_rule,
    sequential_characters_rule,
)



def score_to_rating(score: int) -> str:
    if score <= 30:
        return "Very Weak"
    elif score <= 50:
        return "Weak"
    elif score <= 70:
        return "Moderate"
    elif score <= 85:
        return "Strong"
    else:
        return "Very Strong"


def score_password(password: str) -> dict:
    """
    Runs all password rules and entropy analysis,
    returning a structured result.
    """
    rules = [
        length_rule,
        character_variety_rule,
        repeated_characters_rule,
        sequential_characters_rule,
    ]

    score = 50  # neutral baseline
    issues = []

    # Apply rule-based scoring
    for rule in rules:
        delta, message = rule(password)
        score += delta
        if message:
            issues.append(message)

    # Entropy calculation
    entropy = calculate_entropy(password)

    if entropy < 40:
        score -= 20
        issues.append("Low estimated password entropy")
    elif entropy < 60:
        score -= 5
    elif entropy > 80:
        score += 10

    # Clamp score
    score = max(0, min(100, score))

    rating = score_to_rating(score)

    return {
        "score": score,
        "rating": rating,
        "entropy_bits": entropy,
        "issues": issues,

    "crack_time_estimate": {
    "offline_seconds": estimate_crack_time(entropy, 1_000_000_000),
    "online_seconds": estimate_crack_time(entropy, 100),
}

    }
