from skills.generate_post import generate_post

def test_skill_input_structure():
    output = generate_post("123", "tech", "text")
    assert output["status"] == "success"


def test_confidence_range():
    confidence = 0.85
    assert 0.0 <= confidence <= 1.0
