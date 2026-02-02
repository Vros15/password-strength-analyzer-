from analyzer.rules import length_rule, character_variety_rule


def test_length_rule_too_short():
    score, message = length_rule("abc")
    assert score < 0
    assert message is not None


def test_length_rule_long_password():
    score, message = length_rule("thisIsALongPassword123!")
    assert score > 0
    assert message is None


def test_character_variety_single_type():
    score, message = character_variety_rule("password")
    assert score < 0
    assert message is not None


def test_character_variety_all_types():
    score, message = character_variety_rule("Abc123!")
    assert score > 0
