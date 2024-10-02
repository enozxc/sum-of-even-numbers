def sum_of_even_numbers(numbers: list):
   # sum = 0
   # for number in numbers:
   #     if number % 2 == 0:
   #         sum += number
   # return sum
    return sum(number for number in numbers if number % 2 == 0)


sum_of_even_numbers([]) == 0
sum_of_even_numbers([1, 3, 5, 7]) == 0
sum_of_even_numbers([2, 11, 2, 4]) == 8
