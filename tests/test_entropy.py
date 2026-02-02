from analyzer.entropy import calculate_entropy


def test_entropy_empty_password():
    assert calculate_entropy("") == 0.0


def test_entropy_simple_password():
    entropy = calculate_entropy("password")
    assert entropy < 50


def test_entropy_complex_password():
    entropy = calculate_entropy("Xy9!fQ2$LmR@p")
    assert entropy > 60
