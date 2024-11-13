def get_multiplication(first_number, second_number):
    result = 0
    for _ in range(abs(second_number)):
        result += first_number
    if second_number < 0:
        result = -result
    return result
