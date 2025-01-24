from lab1 import simple_interest, uppercase_count, distance_between_points

def validate_simple_interest():
    test_cases = [
        (1000, 5, 2, 100.0),
        (5, 5, 5, 1.25),
        (500, 20, 10, 1000.0),
    ]

    for principal, rate, years, expected in test_cases:
        result = simple_interest(principal, rate, years)
        assert abs(result - expected) < 1e-2, f"Failed for principal={principal}, rate={rate}, years={years}: {result} != {expected}"

def validate_uppercase_count():
    test_cases = [
        ("Data Science", 2),
        ("DATA", 4),
        ("DATA SCIence", 7),
    ]

    for s, expected in test_cases:
        result = uppercase_count(s)
        assert result == expected, f"Failed for string='{s}': {result} != {expected}"

def validate_distance_between_points():
    test_cases = [
        (1, 1, 4, 5, 5.0),
        (2, 3, 5, 7, 5.0),
        (3, 4, 6, 8, 5.0),
    ]

    for x1, y1, x2, y2, expected in test_cases:
        result = distance_between_points(x1, y1, x2, y2)
        assert abs(result - expected) < 1e-2, f"Failed for points ({x1}, {y1}) to ({x2}, {y2}): {result} != {expected}"

if __name__ == "__main__":
    print("Validating simple_interest...")
    validate_simple_interest()
    print("simple_interest passed.")

    print("Validating uppercase_count...")
    validate_uppercase_count()
    print("uppercase_count passed.")

    print("Validating distance_between_points...")
    validate_distance_between_points()
    print("distance_between_points passed.")
