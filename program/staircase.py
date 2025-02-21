def staircase(n, pattern):
    result = ""
    # Handle case below 1 and above 30
    if n < 1 or n > 30:
        return result
    # Main program
    for i in range(n):
        for _ in range(n - i - 1):
            result += " "
        for _ in range(i + 1):
            result += pattern
        result += "\n"
    return result
