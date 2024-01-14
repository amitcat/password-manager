def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    def calculate_sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    def calculate_count(numbers):
        count = 0
        for num in numbers:
            count += 1
        return count

    return calculate_sum(numbers) / calculate_count(numbers)


numbers = [5, 1, 7, 9]
print(calculate_average(numbers))