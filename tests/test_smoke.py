def test_smoke():
    """Smoke test to ensure pytest discovers at least one test.

    This prevents CI from failing with exit code 5 (no tests collected).
    """
    assert True
