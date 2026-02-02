from analyzer.scorer import score_password


def test_very_weak_password():
    result = score_password("password")
    assert result["rating"] in {"Very Weak", "Weak"}
    assert result["entropy_bits"] < 50
    assert len(result["issues"]) > 0


def test_strong_password():
    result = score_password("Xy9!fQ2$LmR@p")
    assert result["rating"] in {"Strong", "Very Strong"}
    assert result["entropy_bits"] > 60
