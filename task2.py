def find_common_divisors(numbers):
    min_num = min(numbers)
    
    common_divisors = []
    
    for i in range(1, min_num + 1):
        is_common_divisor = True
        for num in numbers:
            if num % i != 0:
                is_common_divisor = False
                break
        if is_common_divisor:
            common_divisors.append(i)
    
    return common_divisors
