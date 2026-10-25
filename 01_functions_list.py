numbers = [1, 2, 3, 4, 5, 6]


def even(numbers):
    new = []
    
    for number in numbers:
        if number % 2 == 0:
            new.append(number)

    return new

result = even(numbers)

print(result)