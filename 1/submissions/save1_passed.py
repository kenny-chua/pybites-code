def sum_numbers(numbers=None):
    if numbers == None:
        return 100 * (100 + 1) // 2
    else:
        return sum(numbers)
        
print(sum_numbers([1, 4, 5]))
print(sum_numbers())