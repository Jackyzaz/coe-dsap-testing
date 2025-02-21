def is_prime_list(numbers):
    # Handle empty numbers
    if numbers == []:
        return False
    # Main logic
    for num in numbers:
        # Handle case 1
        if num <= 1:
            return False
        for n in range(2, num):
            if num % n == 0:
                return False
    return True
