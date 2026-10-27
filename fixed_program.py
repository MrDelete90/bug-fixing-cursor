def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

def find_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

marks = [40, 55, 70, 85]
print("Average:", calculate_average(marks))
print("Largest:", find_largest(marks))
