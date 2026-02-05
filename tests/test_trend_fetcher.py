from skills.trend_fetcher import fetch_trends

def test_trend_data_structure():
    result = fetch_trends()

    assert "topic" in result
    assert "popularity_score" in result
