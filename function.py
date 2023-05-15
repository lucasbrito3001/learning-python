from math import floor

def calc_average(grades = []) -> float:
    total = 0

    for grade in grades:
        total += grade

    return round(total / len(grades), 2)

def calc_median(grades = []) -> float:
    median = 0
    
    grades_length = len(grades)
    is_odd = grades_length % 2 == 0

    grades.sort()

    half_list = floor(grades_length / 2)

    if is_odd == True:
        median = (grades[half_list - 1] + grades[half_list]) / 2
    else:
        median = grades[half_list]
    
    return round(median, 2)

def format_numbers(numbers_list) -> list[int]:
    formatted_numbers = []

    for number in numbers_list.split(','):
        try:
            formatted_number = round(float(number), 2)
            formatted_numbers.append(formatted_number)
        except:
            return 'Invalid data, only numbers are allowed'
    
    print(formatted_numbers)
    return formatted_numbers

numbers = input('Digite os números separados por vírgula: ')

formatted_numbers = format_numbers(numbers)

if(isinstance(formatted_numbers, str)):
    print(formatted_numbers)
else:
    student_average = calc_average(formatted_numbers)
    student_median = calc_median(formatted_numbers)

    print(f"average: {student_average}")
    print(f"median: {student_median}")
